def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[43:96]
    lowercase_substring = substring.lower()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 48, len(substring) + 1)):
            potential_palindrome = lowercase_substring[i:j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                result.add(substring[i:j])
    return result