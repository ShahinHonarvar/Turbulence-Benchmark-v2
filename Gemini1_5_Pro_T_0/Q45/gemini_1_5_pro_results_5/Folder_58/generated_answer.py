from itertools import permutations

def palindromes_between_indices(string):
    letters = set()
    for i in range(7):
        if string[i:i + 1].isalpha():
            letters.add(string[i:i + 1].lower())
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for candidate_tuple in permutations(letters, length):
            candidate = ''.join(candidate_tuple)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes