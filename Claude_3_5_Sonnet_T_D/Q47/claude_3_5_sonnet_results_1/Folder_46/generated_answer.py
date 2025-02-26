def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[11:98]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 29, min(i + 63, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and is_palindrome(word) and (29 <= len(word) <= 62):
                palindromes.add(word)
    return palindromes