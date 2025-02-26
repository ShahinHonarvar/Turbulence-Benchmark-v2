def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[127:289]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result