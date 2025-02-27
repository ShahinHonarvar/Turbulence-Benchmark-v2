def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for r in range(4, len(letters) + 1):
        for p in set(permutations(letters, r)):
            w = ''.join(p)
            if is_palindrome(w):
                palindromes.add(w)
    return palindromes