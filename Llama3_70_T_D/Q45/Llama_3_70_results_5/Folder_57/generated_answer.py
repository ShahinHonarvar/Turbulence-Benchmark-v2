from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:6].lower()
    sub_string = ''.join(filter(str.isalpha, sub_string))
    result = set()
    for r in range(5, len(sub_string) + 1):
        for perm in permutations(sub_string, r):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result