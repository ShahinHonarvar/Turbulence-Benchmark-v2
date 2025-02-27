from itertools import permutations

def palindromes_between_indices(s):
    low_string = s.lower()
    unique_letters = sorted(set(low_string[0:5]))
    permutations_list = list(permutations(unique_letters))
    palindromes = set()
    for perm in permutations_list:
        palindrome = ''.join(perm)
        if palindrome in low_string[0:5]:
            palindromes.add(palindrome)
    return palindromes