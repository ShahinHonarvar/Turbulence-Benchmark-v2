def palindromes_between_indices(s):
    substring = s[3:7].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes