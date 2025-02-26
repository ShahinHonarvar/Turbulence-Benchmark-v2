def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:6] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            rest = chars[:i] + chars[i + 1:]
            for sub_palindrome in generate_palindromes(rest, length - 2):
                palindrome = c + sub_palindrome + c
                if len(palindrome) >= 4:
                    result.add(palindrome)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes