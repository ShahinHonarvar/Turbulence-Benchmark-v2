def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        if len(current) < len(letters):
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes