def palindromes_between_indices(s):
    sub_str = s[6:9].lower()
    sub_str = ''.join(filter(str.isalpha, sub_str))
    palindrome_set = set()
    for p in sub_str:
        if len(p) >= 4 and p == p[::-1]:
            palindrome_set.add(p)
    return palindrome_set