def palindromes_between_indices(s):
    substring = s[2:10]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(6, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            candidate = letters[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes