def palindromes_of_specific_lengths(s):
    substring = s[13:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 57, min(i + 61, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 57 <= len(potential_palindrome) <= 60:
                result.add(potential_palindrome)
    return result