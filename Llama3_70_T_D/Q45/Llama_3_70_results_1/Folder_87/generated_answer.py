def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def form_palindromes(current, remaining):
        if len(current) >= 3:
            if is_palindrome(current):
                palindromes.add(current)
        for i, c in enumerate(remaining):
            form_palindromes(current + c, remaining[:i] + remaining[i + 1:])
    form_palindromes('', letters)
    return palindromes