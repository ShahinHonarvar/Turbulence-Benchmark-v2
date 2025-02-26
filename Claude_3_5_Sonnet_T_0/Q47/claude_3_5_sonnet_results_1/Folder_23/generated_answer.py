def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 56, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 17 <= len(potential_palindrome) <= 55:
                result.add(potential_palindrome)
    return result