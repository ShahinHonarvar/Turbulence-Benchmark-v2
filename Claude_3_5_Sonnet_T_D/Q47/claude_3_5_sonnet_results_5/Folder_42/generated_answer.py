def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[43:96]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 48, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and is_palindrome(word) and (18 <= len(word) <= 47):
                palindromes.add(word)
    return palindromes