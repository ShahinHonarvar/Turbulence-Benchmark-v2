def palindromes_between_indices(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [c.lower() for c in input_string[4:10] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and is_palindrome(current):
            result.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result