from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for perm_length in range(7, len(letters) + 1):
        for perm in permutations(letters, perm_length):
            for i in range(len(perm) - perm_length + 1):
                possible_palindrome = perm[i:i + perm_length]
                if list(possible_palindrome) == list(possible_palindrome)[::-1]:
                    palindromes.add(''.join(possible_palindrome))
    return palindromes