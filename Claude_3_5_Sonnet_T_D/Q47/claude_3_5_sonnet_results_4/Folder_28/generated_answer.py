def palindromes_of_specific_lengths(s):
    substring = s[32:72]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 33, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 21 <= len(potential_palindrome) <= 32:
                result.add(potential_palindrome)
    return result