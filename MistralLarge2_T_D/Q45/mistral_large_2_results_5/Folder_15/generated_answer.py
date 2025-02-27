def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[1:3].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            if is_palindrome(substring[i:j]):
                palindromes.add(substring[i:j])
    return palindromes