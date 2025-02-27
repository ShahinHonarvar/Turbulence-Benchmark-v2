def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(4, 9):
        for j in range(i + 1, 9):
            substring = s[i:j].lower()
            if all((char in english_letters for char in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes