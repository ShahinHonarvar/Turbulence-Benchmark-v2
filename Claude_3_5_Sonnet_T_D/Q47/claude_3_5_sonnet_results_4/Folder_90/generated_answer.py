def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[106:281]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 136, i + 152):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result