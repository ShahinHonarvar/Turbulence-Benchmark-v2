from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch for ch in 'abcdefghi' if ch in s[1:9]]
    palindromes = set()
    for p in permutations(letters, 6):
        word = ''.join(p)
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes