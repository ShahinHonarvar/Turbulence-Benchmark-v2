import itertools

def palindromes_between_indices(text):
    s = set()
    for p in itertools.permutations(list(filter(lambda c: c.isalpha(), text[2:8]))):
        word = ''.join(p).lower()
        if len(word) >= 3 and word == word[::-1]:
            s.add(word)
    return s