from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = s[1:6]
    letter_list = [char for char in sub_string if char.isalpha()]
    palindromes = set()
    for i in range(4, len(letter_list) + 1):
        for perm in permutations(letter_list, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes