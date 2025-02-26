def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[12:123]
    lowercase_substring = substring.lower()
    for length in range(12, 221):
        for i in range(len(lowercase_substring) - length + 1):
            potential_palindrome = lowercase_substring[i:i + length]
            if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
                result.add(substring[i:i + length])
    return result