def palindromes_between_indices(s):
    chars = s[1:3]
    chars = set(chars.lower())
    arrangements = [''.join(i) for i in permutations(chars, len(chars))]
    palindromes = [i for i in arrangements if len(i) >= 3 and i == i[::-1]]
    return set(palindromes)