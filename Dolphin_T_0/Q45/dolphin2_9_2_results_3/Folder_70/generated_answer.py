def palindromes_between_indices(s):
    letters = set(s[1:7].lower())
    palindromes = set()
    if len(letters) < 2:
        return palindromes
    for length in range(4, len(s) + 1):
        for i in range(len(s) - length + 1):
            if set(s[i:i + length].lower()) == letters and s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                palindromes.add(s[i:i + length].lower())
    return palindromes