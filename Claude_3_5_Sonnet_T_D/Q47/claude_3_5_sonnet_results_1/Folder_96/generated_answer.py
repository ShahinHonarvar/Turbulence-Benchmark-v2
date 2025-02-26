def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:301]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 50, min(i + 101, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result