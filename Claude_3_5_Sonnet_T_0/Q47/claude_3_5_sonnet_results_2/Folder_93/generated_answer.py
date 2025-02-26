def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[17:96]
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 50, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 13 <= len(potential_palindrome) <= 49:
                result.add(potential_palindrome)
    return result