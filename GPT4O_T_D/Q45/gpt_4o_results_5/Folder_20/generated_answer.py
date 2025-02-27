from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:9]
    letters = [ch.lower() for ch in sub_string if ch.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            half_len = length // 2
            if perm[:half_len] == perm[:half_len - 1:-1]:
                unique_palindromes.add(''.join(perm))
    return unique_palindromes