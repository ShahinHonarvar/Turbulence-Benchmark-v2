from itertools import permutations

def palindromes_between_indices(text):
    letters = [c.lower() for c in text[1:9] if 'a' <= c.lower() <= 'z']
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes