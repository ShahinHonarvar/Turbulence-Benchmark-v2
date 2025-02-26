def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:73]
    lowercase_substring = substring.lower()
    for length in range(19, 56):
        for i in range(len(substring) - length + 1):
            potential_palindrome = lowercase_substring[i:i + length]
            if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
                result.add(substring[i:i + length])
    return result