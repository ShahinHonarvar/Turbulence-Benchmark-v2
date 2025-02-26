def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    result = set()
    substring = s[10:56]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 8, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and is_palindrome(word):
                result.add(word.lower())
    return result