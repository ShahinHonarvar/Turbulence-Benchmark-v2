from itertools import permutations

def palindromes_between_indices(s):
    lower_s = s.lower()
    relevant_substr = lower_s[6:9]
    valid_chars = [c for c in relevant_substr if c.isalpha()]
    possible_palindromes = set()
    for length in range(3, len(valid_chars) + 1):
        for perm in permutations(valid_chars, length):
            if perm == perm[::-1]:
                possible_palindromes.add(''.join(perm))
    return possible_palindromes