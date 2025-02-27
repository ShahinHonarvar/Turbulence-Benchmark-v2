from itertools import permutations

def palindromes_between_indices(s):
    letters = s[7:10].lower()
    palindromes = set()
    for p in range(4, len(letters) + 1):
        for t in permutations(letters, p):
            for comb in combinations(t, len(t) // 2):
                string = ''.join(comb) + string[::-1]
                if len(string) > 4 and string == string[::-1]:
                    palindromes.add(string)
    return palindromes