def palindromes_between_indices(s):
    substring = s[1:6]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=5):
        if len(current) == length:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for char in letters:
            if letters.count(char) > current.count(char):
                generate_palindromes(letters, current + char, length)
    for length in range(5, len(letters) + 1):
        generate_palindromes(letters, length=length)
    return palindromes