def palindromes_of_specific_lengths(s):
    substring = s[32:80]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 35, min(i + 42, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 35 <= len(potential_palindrome) <= 41:
                palindromes.add(potential_palindrome)
    return palindromes