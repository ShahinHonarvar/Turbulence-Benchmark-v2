def palindromes_of_specific_lengths(string):
    substring = string[11:88]
    palindromes = set(filter(lambda w: len(w) in [4, 5], [substring[i:j] for i in range(len(substring)) for j in range(i + 3, len(substring))]))
    palindromes_lower = set(map(lambda p: p.lower(), palindromes))
    return set(filter(lambda p: p in 'abcdefghijklmnopqrstuvwxyz', palindromes_lower))