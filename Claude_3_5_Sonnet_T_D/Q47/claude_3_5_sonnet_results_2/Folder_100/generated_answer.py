def palindromes_of_specific_lengths(s):
    substring = s[29:97]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 19, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 12 and len(potential_palindrome) <= 18 and (potential_palindrome == potential_palindrome[::-1]):
                result.add(potential_palindrome)
    return result