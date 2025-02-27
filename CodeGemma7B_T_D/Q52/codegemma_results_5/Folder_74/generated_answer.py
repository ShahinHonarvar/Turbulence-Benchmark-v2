from itertools import combinations

def palindrome_of_length_n(string):
    lower_cased_string = string.casefold()
    all_combinations = []
    for i in range(len(lower_cased_string)):
        for j in range(i + 1, len(lower_cased_string) + 1):
            combinations = combinations(lower_cased_string[i:j], 96)
            all_combinations.extend(combinations)
    palindromes = set()
    for combination in all_combinations:
        if combination == combination[::-1]:
            palindromes.add(''.join(combination))
    return palindromes