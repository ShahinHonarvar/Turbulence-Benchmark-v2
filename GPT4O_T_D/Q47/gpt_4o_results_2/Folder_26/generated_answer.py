def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[24:85]
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 32, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            stripped = ''.join(filter(str.isalpha, potential_palindrome)).lower()
            if len(stripped) in range(21, 32) and stripped == stripped[::-1]:
                result.add(potential_palindrome)
    return result