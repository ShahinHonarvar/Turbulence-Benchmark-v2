def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(str.isalpha, s[4:10])))
    return set(filter(lambda x: len(x) >= 4 and x == x[::-1], (''.join(i) for i in letters)))