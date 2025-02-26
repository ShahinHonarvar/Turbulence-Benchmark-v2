def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[35:89]
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 34, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if len(potential_palindrome) >= 24 and len(potential_palindrome) <= 33:
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result