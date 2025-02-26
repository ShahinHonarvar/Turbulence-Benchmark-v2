def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[70:141]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 61, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 3 and potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result