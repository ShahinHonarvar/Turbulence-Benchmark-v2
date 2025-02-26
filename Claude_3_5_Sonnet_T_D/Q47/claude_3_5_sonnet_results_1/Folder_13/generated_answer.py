def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[13:96]
    substring = ''.join((c for c in substring if c.isalpha()))
    substring = substring.lower()
    n = len(substring)
    for i in range(n):
        for length in range(57, 61):
            if i + length > n:
                break
            potential_palindrome = substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result