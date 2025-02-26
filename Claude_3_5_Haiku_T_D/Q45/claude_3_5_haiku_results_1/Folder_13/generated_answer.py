from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:10]
    letter_set = set((char.lower() for char in letters if char.isalpha()))
    palindromes = set()
    for perm_length in range(5, len(letter_set) + 1):
        for perm in permutations(letter_set, perm_length):
            for arrangement in set(permutations(perm + perm[::-1][1:] if len(perm) % 2 == 0 else perm + perm[::-1][1:len(perm)])):
                palindrome = ''.join(arrangement)
                if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes