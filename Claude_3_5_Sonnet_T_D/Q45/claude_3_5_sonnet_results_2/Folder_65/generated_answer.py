def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7].lower()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        result = []
        for i in range(len(chars)):
            for rest in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                palindrome = chars[i] + rest + chars[i]
                if len(palindrome) >= 5:
                    result.append(palindrome)
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes