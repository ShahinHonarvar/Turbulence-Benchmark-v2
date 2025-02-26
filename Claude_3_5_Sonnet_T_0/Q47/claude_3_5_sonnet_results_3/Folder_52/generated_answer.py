def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[44:100]
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 43, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 13 <= len(potential_palindrome) <= 42:
                result.add(potential_palindrome)
    return result