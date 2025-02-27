from itertools import permutations

def palindromes_between_indices(arr):
    substrings = arr[3:8]
    palindromes = set()
    for i in range(5, len(substrings) + 1):
        permutations_i = [''.join(p) for p in permutations(substrings, i)]
        for str in permutations_i:
            if str == ''.join(reversed(str)).lower():
                palindromes.add(str)
    return palindromes