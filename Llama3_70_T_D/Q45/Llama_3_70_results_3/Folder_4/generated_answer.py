from itertools import permutations, combinations_with_replacement

def palindromes_between_indices(s):
    s = s.lower()
    letters = [char for char in s[3:10] if char.isalpha()]
    result = set()
    for length in range(7, len(letters) + 1):
        for combo in combinations_with_replacement(letters, length):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    result.add(word)
    return result