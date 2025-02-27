from collections import Counter
    import itertools

def palindromes_between_indices(string: str) -> set[str]:
    letters = []
    for i in range(1, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(6, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result