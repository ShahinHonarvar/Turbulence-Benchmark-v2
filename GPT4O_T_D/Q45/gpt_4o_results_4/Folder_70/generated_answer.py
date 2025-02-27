from itertools import permutations

def palindromes_between_indices(s):
    selected_string = ''.join(filter(str.isalpha, s[1:7])).lower()
    palindromes = set()
    for length in range(4, len(selected_string) + 1):
        for perm in set(permutations(selected_string, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes