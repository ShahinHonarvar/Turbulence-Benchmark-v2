def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:5] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        result = []
        for i in range(len(chars)):
            for palindrome in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                result.append(chars[i] + palindrome + chars[i])
        return result
    palindromes = set()
    for length in range(5, len(letters) * 2 + 1):
        for palindrome in generate_palindromes(letters, length):
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
    return palindromes