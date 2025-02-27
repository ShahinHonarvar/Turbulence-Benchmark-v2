from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for length in range(5, len(letters) + 1):
        for candidate_tuple in permutations(letters, length):
            candidate_string = ''.join(candidate_tuple)
            if candidate_string == candidate_string[::-1]:
                result.add(candidate_string)
    return result