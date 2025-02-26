def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:8] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in set(chars):
            remaining = chars.replace(char, '', 1)
            for sub_palindrome in generate_palindromes(remaining, length - 2):
                palindrome = char + sub_palindrome + char
                if len(palindrome) >= 6:
                    result.add(palindrome)
        return result
    palindromes = set()
    for length in range(6, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes