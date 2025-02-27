import itertools

def palindromes_between_indices(s):
    english_letters = [char.lower() for char in s[3:9] if char.isalpha()]
    if len(english_letters) < 6:
        return set()
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        for combination in itertools.permutations(english_letters, length):
            combination_str = ''.join(combination)
            if combination_str == combination_str[::-1]:
                palindromes.add(combination_str)
    return palindromes