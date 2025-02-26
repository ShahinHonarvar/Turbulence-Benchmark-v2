def palindromes_of_specific_lengths(s):
    substring = s[41:90]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 39, len(substring) + 1)):
            potential_palindrome = ''.join((c.lower() for c in substring[i:j] if c.isalpha()))
            if len(potential_palindrome) >= 23 and len(potential_palindrome) <= 38:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result