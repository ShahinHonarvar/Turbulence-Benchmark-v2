def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[31:75]
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 40, len(substring) + 1)):
            potential_palindrome = ''.join((c.lower() for c in substring[i:j] if c.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 23 <= len(potential_palindrome) <= 39:
                result.add(potential_palindrome)
    return result