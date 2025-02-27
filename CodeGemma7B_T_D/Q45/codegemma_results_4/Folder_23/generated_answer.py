from itertools import permutations

def palindromes_between_indices(a):
    answer = set()
    for p in permutations(a):
        word = ''.join(p)
        word = word.lower()
        if word >= 'aaaa' and word <= 'z'.zfill(4):
            answer.add(word)
    if not answer:
        return set()
    return answer