from itertools import permutations

def palindrome_between_indices(s):
    letters = ''.join(sorted(set(s[2:8])))
    len_letters = len(letters)
    palindromes = set()
    for length in range(6, len_letters + 1):
        for letters_comb in permutations(letters, length):
            if letters_comb == letters_comb[::-1]:
                palindromes.add(''.join(letters_comb))
    return palindromes