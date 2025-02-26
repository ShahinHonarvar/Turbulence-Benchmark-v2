def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:91]
    for i in range(len(substring)):
        for j in range(i + 27, min(i + 59, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 27 <= len(potential_palindrome) <= 58:
                result.add(potential_palindrome)
    return result