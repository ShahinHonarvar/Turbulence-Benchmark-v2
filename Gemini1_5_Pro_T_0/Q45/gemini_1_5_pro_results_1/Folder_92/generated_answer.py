from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(4, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring) + 1):
                for permutation in permutations(substring, k):
                    word = ''.join(permutation)
                    if len(word) >= 4 and word == word[::-1]:
                        result.add(word)
    return result