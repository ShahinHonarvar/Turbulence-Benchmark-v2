from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    combinations = []
    for i in range(len(s) - 4 + 1):
        for j in range(i + 4):
            combination = s[i:j + 1]
            if combination.lower() not in combinations:
                combinations.append(combination.lower())
    palindromes = []
    for combination in combinations:
        for permutation in permutations(combination):
            word = ''.join(permutation)
            if is_palindrome(word):
                palindromes.append(word)
    return set(palindromes)