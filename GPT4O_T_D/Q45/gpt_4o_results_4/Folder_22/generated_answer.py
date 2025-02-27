import itertools

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[5:7]
    english_letters = [c for c in substr if c.isalpha()]
    palindrome_set = set()
    if len(english_letters) < 3:
        return palindrome_set
    for p_length in range(3, len(english_letters) + 1):
        for perm in itertools.permutations(english_letters, p_length):
            if perm == perm[::-1]:
                palindrome_set.add(''.join(perm))
    return palindrome_set