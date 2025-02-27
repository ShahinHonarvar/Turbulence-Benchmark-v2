from collections import Counter

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(9) if string[i].isalpha()))
    result = set()
    for item in map(lambda p: ''.join(p), letters.elements()):
        if len(item) >= 7 and item == item[::-1]:
            result.add(item)
    return result