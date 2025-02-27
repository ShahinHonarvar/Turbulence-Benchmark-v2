def palindromes_between_indices(s):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_chars = ''.join((c for c in s[1:7].lower() if c in letters))
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current=''):
        if len(current) >= 7 and is_palindrome(current):
            palindromes.add(current)
        if len(chars) > 0:
            for i in range(len(chars)):
                generate_palindromes(chars[:i] + chars[i + 1:], current + chars[i])
    generate_palindromes(filtered_chars)
    return palindromes