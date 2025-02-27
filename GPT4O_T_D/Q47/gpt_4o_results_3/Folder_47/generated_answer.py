def palindromes_of_specific_lengths(s):
    substr = ''.join([c for c in s[39:95] if c.isalpha()]).lower()
    palindromes = set()
    for start in range(len(substr)):
        for end in range(start + 14, min(start + 53, len(substr) + 1)):
            part = substr[start:end]
            if part == part[::-1]:
                palindromes.add(part)
    return palindromes