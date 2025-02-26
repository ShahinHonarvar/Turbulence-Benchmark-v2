def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:6])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            for subpalindrome in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                new_palindrome = c + subpalindrome + c
                if len(new_palindrome) >= 4:
                    result.add(new_palindrome)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes