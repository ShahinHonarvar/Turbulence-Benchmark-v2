def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in chars:
            rest = chars.replace(char, '', 1)
            for sub_palindrome in generate_palindromes(rest, length - 2):
                palindrome = char + sub_palindrome + char
                if len(palindrome) >= 4:
                    result.add(palindrome)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes