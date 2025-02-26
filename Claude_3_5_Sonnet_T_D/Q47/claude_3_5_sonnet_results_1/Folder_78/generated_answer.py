def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:73]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 19, min(i + 56, len(substring) + 1)):
            if j - i > 55:
                break
            potential_palindrome = substring[i:j]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result