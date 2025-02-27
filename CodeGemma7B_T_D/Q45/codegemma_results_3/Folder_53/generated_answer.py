from itertools import permutations

def palindromes_between_indices(string):
    set_of_palindromes = set()
    string = string[4:9].lower()
    for i in range(len(string) - 5):
        for p in permutations(string[i:i + 6]):
            palindrome = ''.join(p)
            set_of_palindromes.add(palindrome)
    return set_of_palindromes