from itertools import permutations

def palindromes_between_indices(text):
    text = ''.join(filter(str.isalpha, text.lower()))
    letters = text[4:10]
    permutations_of_letters = list(permutations(letters))
    palindromes = []
    for permutation in permutations_of_letters:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.append(palindrome)
    return set(palindromes)