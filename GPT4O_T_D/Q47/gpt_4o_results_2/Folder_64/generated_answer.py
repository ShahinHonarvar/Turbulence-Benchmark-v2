def palindromes_of_specific_lengths(s):
    substr = s[:8].lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 4, min(i + 6, len(substr) + 1)):
            part = substr[i:j]
            if all((c.isalpha() for c in part)) and part == part[::-1]:
                palindromes.add(part)
    return palindromes