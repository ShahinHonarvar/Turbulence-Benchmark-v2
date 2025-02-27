from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string.lower()
    sub_string = input_string[4:10]
    palindromes_set = set()
    for length in range(6, len(sub_string) + 1):
        for perm in permutations(sub_string, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes_set.add(word)
    return palindromes_set