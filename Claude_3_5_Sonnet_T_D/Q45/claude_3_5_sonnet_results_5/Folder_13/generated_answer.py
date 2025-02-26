def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[3:10] if char.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        palindromes = []
        for i in range(len(chars)):
            char = chars[i]
            remaining = chars[:i] + chars[i + 1:]
            if length == 1:
                palindromes.append(char)
            else:
                sub_palindromes = generate_palindromes(remaining, length - 2)
                for sub in sub_palindromes:
                    palindromes.append(char + sub + char)
        return palindromes
    result = set()
    for length in range(5, len(letters) + 1):
        palindromes = generate_palindromes(letters, length)
        result.update(filter(is_palindrome, palindromes))
    return result