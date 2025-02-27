def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            substring = ''.join(letters[i:j]).lower()
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes