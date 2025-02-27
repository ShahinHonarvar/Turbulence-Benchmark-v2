from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = s[6:9]
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for p in permutations(chars, length):
            temp = ''.join(p)
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes