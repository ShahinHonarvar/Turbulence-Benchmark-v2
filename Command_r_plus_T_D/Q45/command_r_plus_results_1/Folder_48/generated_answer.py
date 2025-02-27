def palindromes_between_indices(s):
    s = s.lower()
    subset = set(s[6:9])
    palindromes = set()
    for char in subset:
        if s.count(char) >= 2:
            palindromes.add(char * 2)
    return palindromes