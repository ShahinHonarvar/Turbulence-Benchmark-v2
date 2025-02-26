def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[4:9] if char.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in set(chars):
            remaining = list(chars)
            remaining.remove(char)
            for sub_palindrome in generate_palindromes(remaining, length - 2):
                palindrome = char + sub_palindrome + char
                if len(palindrome) >= 4:
                    result.add(palindrome)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes