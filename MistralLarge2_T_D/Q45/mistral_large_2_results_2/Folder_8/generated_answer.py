def palindromes_between_indices(s):
    letters = [char for char in s[1:6] if char.isalpha()]
    letters = [char.lower() for char in letters]
    n = len(letters)

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(5, n + 1):
        for start in range(n - length + 1):
            word = ''.join(letters[start:start + length])
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes