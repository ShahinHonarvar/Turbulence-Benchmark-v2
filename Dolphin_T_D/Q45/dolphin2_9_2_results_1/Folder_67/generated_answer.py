import itertools

def palindromes_between_indices(s):
    letters = set([ch for ch in s.lower() if ch.isalpha()])
    length = 7
    if len(letters) < 5:
        return set()
    result = set()
    for p in itertools.product(letters, repeat=length // 2):
        word = ''.join(p) + ('' if length % 2 == 0 else p[-1])
        if word == word[::-1]:
            result.add(word)
    return result