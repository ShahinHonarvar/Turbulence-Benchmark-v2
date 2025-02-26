def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[39:95]
    for i in range(len(substring)):
        for j in range(i + 14, min(i + 53, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 14 <= len(potential_palindrome) <= 52:
                result.add(potential_palindrome)
    return result