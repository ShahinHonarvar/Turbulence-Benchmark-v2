def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 34, min(i + 56, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if len(potential_palindrome) >= 34 and len(potential_palindrome) <= 55:
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    palindromes.add(potential_palindrome)
    return palindromes