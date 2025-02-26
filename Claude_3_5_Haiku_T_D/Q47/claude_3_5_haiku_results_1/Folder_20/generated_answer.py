def palindromes_of_specific_lengths(s):

    def is_valid_palindrome(palindrome):
        return palindrome.isalpha() and palindrome == palindrome[::-1]
    substring = s[20:75]
    result = set()
    for length in range(36, 43):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if is_valid_palindrome(candidate):
                result.add(candidate)
    return result