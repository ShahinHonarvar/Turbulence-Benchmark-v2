from collections import Counter

def palindromes_between_indices(text):
    letters = Counter(text[3:9].lower())
    result = set()
    for i in range(6, 9):
        for perm in permutate_letters(letters, i):
            if perm == perm[::-1]:
                result.add(perm)
    return result

def permutate_letters(letters, length):
    if length == 0:
        yield ''
    else:
        for letter, count in letters.items():
            if count > 0:
                letters[letter] -= 1
                for perm in permutate_letters(letters, length - 1):
                    yield (letter + perm)
                letters[letter] += 1