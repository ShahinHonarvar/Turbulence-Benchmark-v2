def palindromes_of_specific_lengths(s):
    s = s[10:84]
    letters_only = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters_only)):
        for j in range(i, min(i + 61, len(letters_only))):
            if letters_only[i:j + 1] == letters_only[i:j + 1][::-1]:
                palindromes.add(letters_only[i:j + 1])
    return set((pal for pal in palindromes if len(pal) >= 37 and len(pal) <= 60))