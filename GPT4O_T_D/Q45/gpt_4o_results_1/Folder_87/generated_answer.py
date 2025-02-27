from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[3:10].lower()
    filtered_chars = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(filtered_chars):
        for length in range(3, len(filtered_chars) + 1):
            half = length // 2
            if perm[:half] == perm[length - half:length][::-1]:
                palindromes.add(''.join(perm[:length]))
    return palindromes