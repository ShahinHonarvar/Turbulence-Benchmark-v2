from itertools import permutations 

def palindromes_between_indices(s):
    palindromes = set()
    substring = s[5:9]
    for p in permutations(substring, 3):
        temp = ''.join(p).lower()
        if temp == temp[::-1]:
            palindromes.add(temp)
    return palindromes