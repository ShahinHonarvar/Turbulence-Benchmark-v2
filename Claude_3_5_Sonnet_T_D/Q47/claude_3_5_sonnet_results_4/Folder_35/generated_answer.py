def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 14, min(i + 40, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 14 <= len(potential_palindrome) <= 39:
                result.add(potential_palindrome)
    return result