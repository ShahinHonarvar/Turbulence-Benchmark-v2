def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:8].lower()))
    palindromes = set()
    for i in range(len(letters) - 6):
        for j in range(i + 7, len(letters) + 1):
            candidate = letters[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes