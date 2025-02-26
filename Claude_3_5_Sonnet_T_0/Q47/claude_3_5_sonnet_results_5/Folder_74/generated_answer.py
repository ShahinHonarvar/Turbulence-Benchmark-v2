def palindromes_of_specific_lengths(s):
    substring = s[30:85]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 21, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 12 <= len(potential_palindrome) <= 20:
                result.add(potential_palindrome)
    return result