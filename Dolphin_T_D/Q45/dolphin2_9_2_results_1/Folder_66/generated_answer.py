def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    letters = [c for c in s[:6] if c.isalpha()]
    if len(letters) < 5:
        return set()
    letters = sorted(set(letters))
    result = set()

    def generate_palindromes(curr, word):
        if len(curr) >= 5 and is_palindrome(curr):
            result.add(''.join(curr))
        if len(word) == 0:
            return
        for i, c in enumerate(word):
            generate_palindromes(curr + word[i:i + 1], word[:i] + word[i + 1:])
    generate_palindromes([], ''.join(letters))
    return result