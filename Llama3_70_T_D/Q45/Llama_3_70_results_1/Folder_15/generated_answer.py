def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for c in letters:
        remaining = letters[:]
        remaining.remove(c)
        for d in remaining:
            remaining2 = remaining[:]
            remaining2.remove(d)
            for e in remaining2:
                palindrome = c + d + e
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes