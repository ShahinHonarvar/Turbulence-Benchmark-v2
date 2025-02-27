def palindromes_between_indices(s):
    substring = s[2:5]
    palindromes = set()
    for p in range(4, len(substring) + 1):
        for c in itertools.combinations(substring, p):
            new_string = ''.join(c).lower()
            if new_string == new_string[::-1]:
                palindromes.add(new_string)
    return palindromes