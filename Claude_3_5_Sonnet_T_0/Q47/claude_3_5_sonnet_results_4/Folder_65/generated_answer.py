def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:96]
    for i in range(len(substring)):
        for j in range(i + 20, min(i + 67, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 20 <= len(potential_palindrome) <= 66:
                result.add(potential_palindrome)
    return result