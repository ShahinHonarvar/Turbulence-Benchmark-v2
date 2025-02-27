def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    result = set()
    substring = s[12:93]
    length = len(substring)
    for i in range(length):
        for j in range(i + 17, min(i + 67, length + 1)):
            palindrome = substring[i:j]
            if palindrome.isalpha() and is_palindrome(palindrome.lower()):
                result.add(palindrome.lower())
    return result