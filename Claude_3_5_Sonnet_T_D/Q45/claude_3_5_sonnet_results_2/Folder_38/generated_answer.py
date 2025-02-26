def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[3:9] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        result = []
        for i, char in enumerate(chars):
            for palindrome in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                result.append(char + palindrome + char)
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for palindrome in generate_palindromes(letters, length):
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes