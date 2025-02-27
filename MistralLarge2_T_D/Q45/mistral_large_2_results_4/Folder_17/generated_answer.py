def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[2:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            candidate = letters[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes