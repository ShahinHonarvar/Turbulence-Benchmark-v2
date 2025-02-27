def palindromes_between_indices(s):
    substring = s[2:6]
    palindromes = set()
    for p in range(5, len(substring)):
        if substring[:p] == substring[:p][::-1]:
            palindromes.add(substring[:p].lower())
    return palindromes