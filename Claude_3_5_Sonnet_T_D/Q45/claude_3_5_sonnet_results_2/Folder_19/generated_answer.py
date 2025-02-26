def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()
    result = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 7:
            if is_palindrome(current):
                result.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result