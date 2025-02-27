from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = text[5:10]
    p = [''.join(p) for i in range(len(s) + 1) for p in permutations(s, i)]
    for item in p:
        if len(item) >= 6 and item.lower() == item[::-1].lower():
            result.add(item.lower())
    return result