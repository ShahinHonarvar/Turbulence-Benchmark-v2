def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    substring = s[4:10].lower()
    for i in range(6, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            word = substring[j:j + i]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes