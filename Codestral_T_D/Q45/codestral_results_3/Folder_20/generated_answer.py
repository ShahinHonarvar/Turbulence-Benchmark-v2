from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[2:9].lower()
    palindromes = set()
    for length in range(4, len(sub_string) + 1):
        for perm in permutations(sub_string, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes