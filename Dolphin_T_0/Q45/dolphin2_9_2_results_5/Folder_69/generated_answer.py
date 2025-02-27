def palindromes_between_indices(s):
    chars = [ch.lower() for ch in s[:4] if ch.isalpha()]
    palindromes = set()

    def is_palindrome(pal):
        return pal == pal[::-1]

    def generate_palindromes(pal, prefix=''):
        if len(pal) >= 4 and is_palindrome(pal):
            palindromes.add(pal)
        for ch in chars:
            generate_palindromes(pal + ch, prefix + ch)
    if chars:
        generate_palindromes(''.join(chars))
    return palindromes