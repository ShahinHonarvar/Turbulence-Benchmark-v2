from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[4:10].lower()
    palindromes = set()
    for i in range(7, 11):
        for p in permutations(sub_string, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes