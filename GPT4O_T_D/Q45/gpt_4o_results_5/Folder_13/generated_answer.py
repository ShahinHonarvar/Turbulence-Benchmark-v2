from itertools import permutations

def palindromes_between_indices(s):
    sub_string = ''.join([ch for ch in s[3:10].lower() if ch.isalpha()])
    result = set()
    for p in permutations(sub_string):
        word = ''.join(p)
        if len(word) >= 5 and word == word[::-1]:
            result.add(word)
    return result