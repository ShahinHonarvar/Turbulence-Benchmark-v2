def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[40:95]
    for i in range(len(substring)):
        for j in range(i + 45, min(i + 52, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 45 <= len(potential_palindrome) <= 51:
                result.add(potential_palindrome)
    return result