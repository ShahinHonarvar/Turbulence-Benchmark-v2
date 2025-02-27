from itertools import permutations

def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 8):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for candidate_tuple in permutations(letters, length):
            candidate = ''.join(candidate_tuple)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes