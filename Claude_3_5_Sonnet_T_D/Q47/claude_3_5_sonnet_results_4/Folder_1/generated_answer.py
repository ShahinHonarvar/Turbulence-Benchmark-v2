def palindromes_of_specific_lengths(s):
    substring = s[15:90]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 40, min(i + 73, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 40 <= len(potential_palindrome) <= 72:
                result.add(potential_palindrome)
    return result