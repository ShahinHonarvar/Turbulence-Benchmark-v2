from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [char for char in s[3:6] if char.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                if palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes