def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:84]
    lowercase_substring = substring.lower()
    for i in range(len(lowercase_substring)):
        for j in range(i + 13, min(i + 67, len(lowercase_substring) + 1)):
            potential_palindrome = lowercase_substring[i:j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                result.add(substring[i:j])
    return result