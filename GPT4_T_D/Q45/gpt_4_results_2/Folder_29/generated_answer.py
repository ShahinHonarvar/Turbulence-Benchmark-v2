from itertools import permutations

def palindromes_between_indices(input_str):
    processed_str = ''.join((char.lower() for char in input_str[2:10] if char.isalpha()))
    palindromes = set()
    for i in range(6, len(processed_str) + 1):
        for subset in permutations(processed_str, i):
            word = ''.join(subset)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes