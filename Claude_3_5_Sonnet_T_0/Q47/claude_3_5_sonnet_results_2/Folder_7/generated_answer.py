def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[119:257]
    for i in range(len(substring)):
        for j in range(i + 104, min(i + 124, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 104 and len(potential_palindrome) <= 123 and (potential_palindrome == potential_palindrome[::-1]):
                result.add(potential_palindrome)
    return result