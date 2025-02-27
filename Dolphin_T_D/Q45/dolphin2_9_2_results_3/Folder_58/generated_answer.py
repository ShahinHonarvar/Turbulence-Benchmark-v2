import itertools

def palindromes_between_indices(s):
    sub_string = s[:7].lower()
    palindrome_set = set()
    for i in range(6, len(sub_string)):
        for p in itertools.permutations(sub_string, i):
            p = ''.join(p)
            if p == p[::-1] and len(p) >= 6:
                palindrome_set.add(p)
    return palindrome_set