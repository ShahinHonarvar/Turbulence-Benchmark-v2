def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:83]
    for i in range(len(substring) - 31):
        for length in range(32, 35):
            if i + length <= len(substring):
                potential_palindrome = ''.join((c.lower() for c in substring[i:i + length] if c.isalpha()))
                if potential_palindrome == potential_palindrome[::-1] and len(potential_palindrome) == length:
                    result.add(potential_palindrome)
    return result