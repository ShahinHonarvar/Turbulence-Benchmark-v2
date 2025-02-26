def palindromes_of_specific_lengths(s):
    substring = s[27:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 49, min(i + 52, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 49 and len(potential_palindrome) <= 51:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result