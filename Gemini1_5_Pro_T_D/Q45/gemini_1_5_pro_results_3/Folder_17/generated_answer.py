from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 7):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for candidate_tuple in permutations(letters, length):
            candidate = ''.join(candidate_tuple)
            if candidate == candidate[::-1] and len(candidate) >= 4:
                palindromes.add(candidate)
    return palindromes