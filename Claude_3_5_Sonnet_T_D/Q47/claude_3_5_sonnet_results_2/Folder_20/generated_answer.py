def palindromes_of_specific_lengths(string):
    substring = string[20:75]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 36, min(i + 43, len(substring) + 1)):
            potential_palindrome = ''.join((c.lower() for c in substring[i:j] if c.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 36 <= len(potential_palindrome) <= 42:
                palindromes.add(potential_palindrome)
    return palindromes