def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', result=set()):
        if len(current) >= 4 and is_palindrome(current):
            result.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char, result)
        return result
    return generate_palindromes(letters)