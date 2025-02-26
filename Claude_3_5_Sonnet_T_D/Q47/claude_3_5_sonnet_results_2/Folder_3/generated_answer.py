def palindromes_of_specific_lengths(s):
    substring = s[27:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 49, min(i + 52, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if len(potential_palindrome) in [49, 50, 51]:
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result