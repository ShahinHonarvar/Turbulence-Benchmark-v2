from itertools import permutations

def palindromes_between_indices(txt):
    combinations = permutations(txt[3:9])
    Palindromes = set()
    for comb in combinations:
        arr = list(comb)
        arr.extend(comb)
        string_palindrome = ''.join(arr)
        word = string_palindrome.lower()
        if word == word[::-1]:
            Palindromes.add(word)
    return Palindromes