from itertools import permutations

def palindrome_of_length_n(word):
    word = word.lower()
    set_pallindromes = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            for p in permutations(word[i:j]):
                palindrome = ''.join(p)
                if len(palindrome) == 28:
                    set_pallindromes.add(palindrome)
    return set_pallindromes