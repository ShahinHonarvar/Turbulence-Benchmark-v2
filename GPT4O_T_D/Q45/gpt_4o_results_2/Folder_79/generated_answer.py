from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[1:8].lower()
    result = set()

    def is_palindrome(half, additional=None):
        if additional is not None:
            return half + additional + half[::-1]
        return half + half[::-1]

    def generate_halves(remaining, half):
        if len(half) >= 2:
            result.add(is_palindrome(half))
        for i, char in enumerate(remaining):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            generate_halves(remaining[:i] + remaining[i + 1:], half + char)

    def odd_palindrome(remaining, half):
        for i, char in enumerate(remaining):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            result.add(is_palindrome(half, char))
    sorted_chars = ''.join(sorted([c for c in s if c in ascii_lowercase]))
    generate_halves(sorted_chars, '')
    odd_palindrome(sorted_chars, '')
    return {p for p in result if len(p) >= 3}