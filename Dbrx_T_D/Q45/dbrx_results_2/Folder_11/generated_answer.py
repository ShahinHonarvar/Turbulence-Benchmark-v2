def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 8:
        return set()
    substr = s[3:8]
    letters = set((c for c in substr if c.isalpha()))
    if len(letters) < 2:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            sublist = list(letters)
            sublist[i:j + 1] = sublist[j:i - 1:-1]
            palindrome = ''.join(sublist)
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes