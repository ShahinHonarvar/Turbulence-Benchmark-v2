def palindromes_between_indices(string):
    substring = string[6:10].lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            word = substring[i:j]
            if is_palindrome(word) and len(word) >= 3:
                palindromes.add(word)
    return palindromes