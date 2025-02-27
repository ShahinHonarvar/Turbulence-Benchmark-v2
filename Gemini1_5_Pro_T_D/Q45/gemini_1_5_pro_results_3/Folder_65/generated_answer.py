import itertools

def palindromes_between_indices(string: str) -> set[str]:
    letters = []
    for i in range(7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in itertools.permutations(letters, i):
            current = ''.join(j)
            if len(current) >= 5 and current == current[::-1]:
                result.add(current)
    return result