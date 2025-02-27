from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    letter_counter = Counter(''.join(filter(str.isalpha, s[:8])))
    lengths = list(range(3, 7))
    combinations_counter = [[Counter(letters) for letters in permutations(letter_counter.elements(), length)] for length in lengths]
    palindromes = []
    for i, length in enumerate(lengths):
        for j, combination in enumerate(combinations_counter[i]):
            for k in permutations(combination.elements()):
                pal_str = ''.join(k)
                if pal_str == pal_str[::-1]:
                    palindromes.append(pal_str)
    return set(palindromes) if palindromes else ''