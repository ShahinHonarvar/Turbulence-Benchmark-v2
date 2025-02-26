def palindromes_of_specific_lengths(s):
    substring = s[23:78]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 41, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if 13 <= len(potential_palindrome) <= 40 and potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result