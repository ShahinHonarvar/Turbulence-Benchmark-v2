def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.lower() in 'abcdefghijklmnopqrstuvwxyz', s[4:9]))
    return set(filter(lambda x: len(x) >= 4 and x == x[::-1], map(''.join, permutations(letters, len(letters)))))