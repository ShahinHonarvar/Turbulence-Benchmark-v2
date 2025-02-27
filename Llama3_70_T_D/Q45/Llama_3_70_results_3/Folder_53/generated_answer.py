def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = [c for c in s if c.isalpha()]
    letters_set = set(letters)
    palindromes_set = set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 6 and is_palindrome(current):
            palindromes_set.add(current)
        if not remaining:
            return
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    if len(letters_set) > 0:
        generate_palindromes('', letters)
    return palindromes_set