import itertools
    from collections import Counter

def palindromes_between_indices(s):
    counter = Counter(filter(str.isalpha, s[:8]))
    palindromes = set()
    for r in range(7, len(counter) + 1):
        for combination in itertools.combinations(counter.elements(), r):
            combo_counter = Counter(combination)
            if all((combo_counter[char] % 2 == 0 for char in combo_counter)):
                half_str = ''.join((char * (combo_counter[char] // 2) for char in combo_counter))
                palindromes.add(half_str.lower() + half_str.lower()[::-1])
    return palindromes