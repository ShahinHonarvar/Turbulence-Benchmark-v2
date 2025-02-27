def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def get_palindromes(letters):
        palindromes = set()
        n = len(letters)
        for i in range(n):
            for j in range(i + 3, n + 1):
                sub = letters[i:j]
                if is_palindrome(sub):
                    palindromes.add(sub.lower())
        return palindromes
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    return get_palindromes(letters)