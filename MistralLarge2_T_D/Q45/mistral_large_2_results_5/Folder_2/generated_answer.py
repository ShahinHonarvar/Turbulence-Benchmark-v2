def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letters = set(substring)
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(arr, prefix=''):
        if len(prefix) >= 6:
            if is_palindrome(prefix):
                palindromes.add(prefix)
        for char in arr:
            generate_palindromes(arr, prefix + char)
    generate_palindromes(letters)
    return palindromes