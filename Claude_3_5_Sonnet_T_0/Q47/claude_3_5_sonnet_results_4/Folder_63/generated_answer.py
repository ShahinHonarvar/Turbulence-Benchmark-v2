def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[33:86]
    for i in range(len(substring)):
        for j in range(i + 26, min(i + 32, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 26 <= len(potential_palindrome) <= 31:
                result.add(potential_palindrome)
    return result