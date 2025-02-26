def palindromes_of_specific_lengths(s):
    substring = s[36:93]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 36, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 10 <= len(potential_palindrome) <= 35:
                palindromes.add(potential_palindrome)
    return palindromes