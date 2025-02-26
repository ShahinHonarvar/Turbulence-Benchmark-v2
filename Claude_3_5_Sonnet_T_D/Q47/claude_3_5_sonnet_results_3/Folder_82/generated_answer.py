def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    substring = s[3:301]
    for length in range(30, 301):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result