from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        for i in range(len(perm) - 5):
            for j in range(len(perm) - 5 - i + 1):
                candidate = perm[i:i + j + 6]
                if len(candidate) >= 6:
                    palindrome = ''.join(candidate)
                    if palindrome == palindrome[::-1]:
                        unique_palindromes.add(palindrome)
    return unique_palindromes