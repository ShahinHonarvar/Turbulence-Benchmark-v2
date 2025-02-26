def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    result = set()
    substring = s[27:96]
    for start in range(len(substring)):
        for length in range(49, 52):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate):
                result.add(candidate)
    return result