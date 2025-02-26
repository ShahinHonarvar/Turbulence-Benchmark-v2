from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[6:10] if char.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                subset = perm[i:j]
                if len(subset) >= 3:
                    palindrome = ''.join(subset + subset[::-1])
                    if palindrome == palindrome[::-1]:
                        unique_palindromes.add(palindrome)
    return unique_palindromes