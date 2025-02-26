def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    result = set()
    substring = s[29:99]
    for length in range(6, 10):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_palindrome(candidate):
                result.add(candidate)
    return result