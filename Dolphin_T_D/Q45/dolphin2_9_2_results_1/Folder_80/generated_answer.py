def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[3:9] if c.isalpha()]))
    palindromes = set()
    for p in range(7, len(letters) + 1):
        for i in range(len(letters) - p + 1):
            if letters[i:i + p] == letters[i:i + p][::-1]:
                palindromes.add(letters[i:i + p])
    return palindromes