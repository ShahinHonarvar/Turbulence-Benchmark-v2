from itertools import product

def palindrome_of_length_n(strn, n=14):
    result = set()
    if not strn or n == 0:
        return result
    strn = strn.lower()
    for r in range(n):
        for l in range(n - r):
            palindrome = strn[l:l + r + 1]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result