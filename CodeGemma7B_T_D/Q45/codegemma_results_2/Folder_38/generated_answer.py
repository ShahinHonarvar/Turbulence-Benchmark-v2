from itertools import permutations

def palindromes_between_indices(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, 9):
        if len(set(string[i:i + 5]).intersection(english_letters)) >= 5:
            for p in permutations(string[i:i + 5]):
                if ''.join(p).lower() != string[i:i + 5].lower():
                    palindromes.add(''.join(p).lower())
    return palindromes