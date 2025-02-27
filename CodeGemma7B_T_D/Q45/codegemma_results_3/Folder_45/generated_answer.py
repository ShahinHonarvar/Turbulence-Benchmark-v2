from itertools import permutations

def palindromes_between_indices(text):
    words = list(text[5:10])
    if not any((char.isalpha() for char in words)):
        return set()
    result = set()
    for word in words:
        word = word.lower()
        for permutation in permutations(word):
            palindrome = ''.join(permutation)
            if len(palindrome) >= 4:
                result.add(palindrome)
    return result