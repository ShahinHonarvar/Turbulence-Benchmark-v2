def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[22:96]
    for i in range(len(substring)):
        for j in range(i + 52, min(i + 56, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if len(potential_palindrome) >= 52 and len(potential_palindrome) <= 55:
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result