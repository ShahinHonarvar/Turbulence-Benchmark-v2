from itertools import permutations

def palindromes_between_indices(string):
    size = len(string)
    english_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for i in range(size):
        for j in range(size):
            if abs(i - j) >= 6:
                start_index = max(i, j) + 1
                end_index = min(i + 4, j - 4) + 1
                substring = string[start_index:end_index]
                if substring.lower() == substring[::-1].lower():
                    for permutation in permutations(substring):
                        result.add(''.join(permutation))
    return result