from itertools import permutations

def palindromes_between_indices(s):
    eng_letters = [c for c in s.lower() if 'a' <= c <= 'z']
    if len(eng_letters) < 4 or len(s) < 10:
        return set()
    palindromes = set()
    for i in range(len(eng_letters) - 3):
        for j in range(i + 1, len(eng_letters) - 2):
            sub_s = eng_letters[i:j + 1]
            if sub_s == sub_s[::-1]:
                palindromes.add(''.join(sub_s))
    return palindromes