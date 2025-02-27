from itertools import combinations

def palindromes_between_indices(s):
    palindromes = set()
    sub_s = [c for c in s[2:10]]
    for i in range(6, 11):
        for combo in combinations(sub_s, i):
            word = ''.join(combo)
            rev_word = word[::-1]
            if word == rev_word:
                palindromes.add(word.lower())
    return palindromes