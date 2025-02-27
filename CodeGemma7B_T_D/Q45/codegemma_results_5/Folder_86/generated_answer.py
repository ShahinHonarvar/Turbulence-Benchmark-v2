from itertools import permutations

def palindromes_between_indices(text):
    letters = set()
    for letter in text[6:10].lower():
        if letter.isalpha():
            letters.add(letter)
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        for i in range(4, len(perm) + 4):
            palindrome = ''.join(perm[:i][::-1] + perm[i:])
            palindromes.add(palindrome)
    return palindromes