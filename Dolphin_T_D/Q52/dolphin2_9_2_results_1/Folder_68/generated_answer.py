def palindrome_of_length_n(s):
    if len(s) < 76:
        return set()
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 75):
        sub = s[i:i + 76]
        palin = ''.join(reversed(sub))
        if palin == sub:
            palindromes.add(sub)
    return palindromes