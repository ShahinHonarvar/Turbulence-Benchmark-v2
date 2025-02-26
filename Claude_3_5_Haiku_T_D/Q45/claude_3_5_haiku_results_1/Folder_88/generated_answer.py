from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:8] if char.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 6)):
        for middle in range(6):
            candidate = list(perm[:middle] + perm[middle::-1] + perm[middle + 1:])
            palindrome = ''.join(candidate)
            if palindrome == palindrome[::-1]:
                unique_palindromes.add(palindrome)
    return unique_palindromes