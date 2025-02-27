from itertools import permutations

def palindromes_between_indices(string):
    string = string[:6].lower()
    set_of_palindromes = set()
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and i <= j:
                set_of_palindromes.add(string[i:j + 1])
    for i in permutations(string):
        if len(i) >= 3 and i == i[::-1]:
            set_of_palindromes.add(''.join(i))
    return set_of_palindromes