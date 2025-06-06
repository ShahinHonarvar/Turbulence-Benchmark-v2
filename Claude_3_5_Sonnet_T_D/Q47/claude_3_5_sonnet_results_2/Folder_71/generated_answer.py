def palindromes_of_specific_lengths(s):
    substring = s[18:66]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 37, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 23 <= len(potential_palindrome) <= 36:
                result.add(potential_palindrome)
    return result