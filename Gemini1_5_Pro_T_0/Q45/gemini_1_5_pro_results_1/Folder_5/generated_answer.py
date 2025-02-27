from collections import Counter

def palindromes_between_indices(string):
    string = string[4:9].lower()
    letters = [letter for letter in string if letter.isalpha()]
    palindrome_set = set()
    if len(letters) >= 4:
        for size in range(4, len(letters) + 1):
            for permutation in find_permutations(letters, size):
                word = ''.join(permutation)
                if word == word[::-1]:
                    palindrome_set.add(word)
    return palindrome_set

def find_permutations(letters, size):
    if size == 1:
        return [[letter] for letter in letters]
    permutations = []
    for i in range(len(letters)):
        remaining_letters = letters[:i] + letters[i + 1:]
        for permutation in find_permutations(remaining_letters, size - 1):
            permutations.append([letters[i]] + permutation)
    return permutations