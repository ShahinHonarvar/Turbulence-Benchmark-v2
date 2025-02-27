def palindromes_between_indices(s):
    subset = s[2:6]
    letters = ''.join(filter(str.isalpha, subset)).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(prefix, remaining, length):
        if length == 0:
            if is_palindrome(prefix):
                palindromes.add(prefix)
        else:
            for i, char in enumerate(remaining):
                generate_palindromes(prefix + char, remaining[:i] + remaining[i + 1:], length - 1)
    for length in range(4, len(letters) + 1):
        generate_palindromes('', letters, length)
    return palindromes