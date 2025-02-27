def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    letters = get_english_letters(s[1:6])
    palindromes = set()
    length = len(letters)
    for i in range(length):
        for j in range(i + 3, length + 1):
            substring = letters[i:j]
            if is_palindrome(substring) and len(substring) >= 6:
                palindromes.add(substring)
    return palindromes