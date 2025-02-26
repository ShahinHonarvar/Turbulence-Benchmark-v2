def palindromes_of_specific_lengths(s):
    substring = s[17:73]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 50, min(i + 52, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 50 <= len(potential_palindrome) <= 51:
                result.add(potential_palindrome)
    return result