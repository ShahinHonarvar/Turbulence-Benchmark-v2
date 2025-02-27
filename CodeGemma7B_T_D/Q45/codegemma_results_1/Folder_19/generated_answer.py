from itertools import permutations

def palindromes_between_indices(text):
    between_indices = {i for i in range(1, 8) if text[i].lower() in English_letters}
    palindromes = set()
    for char_set in permutations(between_indices):
        temp = text[next(iter(char_set)) + 1:next(iter(char_set)) + 7]
        if temp.lower() == temp[::-1].lower():
            palindromes.add(temp)
    return palindromes