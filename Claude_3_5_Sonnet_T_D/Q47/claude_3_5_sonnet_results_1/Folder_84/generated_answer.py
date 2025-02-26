def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:78]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 41, len(substring) + 1)):
            if j - i > 40:
                break
            potential_palindrome = substring[i:j]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result