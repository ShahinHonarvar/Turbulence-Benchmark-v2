def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[13:96]
    lowercase_substring = substring.lower()
    for i in range(len(substring)):
        for length in range(57, 61):
            if i + length <= len(substring):
                potential_palindrome = lowercase_substring[i:i + length]
                if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
                    result.add(substring[i:i + length])
    return result