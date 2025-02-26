def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:85]
    for i in range(len(substring)):
        for j in range(i + 30, min(i + 47, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 30 <= len(potential_palindrome) <= 46:
                result.add(potential_palindrome)
    return result