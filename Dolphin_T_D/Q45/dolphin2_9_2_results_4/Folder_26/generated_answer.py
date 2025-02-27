def palindromes_between_indices(s):
    sub_s = s[4:7]
    sub_s_set = set((''.join(p) for p in permutations(sub_s)))
    palindrome_set = {i for i in sub_s_set if len(i) >= 3 and i == i[::-1]}
    return palindrome_set