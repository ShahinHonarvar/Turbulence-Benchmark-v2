from itertools import permutations

def palindromes_between_indices(str):
    letters = []
    for char in str:
        if char.isalpha():
            letters.append(char.lower())
    if len(letters) < 4 or letters[2] > letters[5]:
        return set()
    permutations_of_letters = permutations(letters[2:6])
    palindromes = set()
    for permutation in permutations_of_letters:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes