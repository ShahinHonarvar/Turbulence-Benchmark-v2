def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes