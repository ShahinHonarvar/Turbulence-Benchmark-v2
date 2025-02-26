def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[36:93]
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 36, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 10 and potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result