def palindromes_of_specific_lengths(s):
    substring = s[23:83]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 32, min(i + 35, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 32 <= len(potential_palindrome) <= 34:
                result.add(potential_palindrome)
    return result