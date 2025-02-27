def palindromes_between_indices(s):
    substring = s[3:7]
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()

    def is_palindrome(substring):
        return substring == substring[::-1]
    if len(letters) < 3:
        return palindromes
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            new_word = ''.join(letters[i:j]).lower()
            if is_palindrome(new_word):
                palindromes.add(new_word)
    return palindromes