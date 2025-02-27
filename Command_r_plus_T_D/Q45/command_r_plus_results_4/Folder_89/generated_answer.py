def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(5, min(len(s), 10)):
        substring = s[5:i]
        if substring == substring[::-1] and len(substring) >= 6:
            palindromes.add(substring)
    return palindromes