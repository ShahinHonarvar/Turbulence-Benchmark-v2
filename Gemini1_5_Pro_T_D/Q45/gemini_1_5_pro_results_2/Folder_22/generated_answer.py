from itertools import permutations

def palindromes_between_indices(text):
    letters = [text[i].lower() for i in range(5, 7) if text[i].isalpha()]
    result = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters, i):
                candidate = ''.join(p)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result