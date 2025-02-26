from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:9] if char.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            mid = len(candidate) // 2
            if len(candidate) % 2 == 0:
                left = candidate[:mid]
                right = candidate[mid:]
                right.reverse()
            else:
                left = candidate[:mid]
                right = candidate[mid + 1:]
                right.reverse()
            if left == right:
                palindrome = ''.join(candidate)
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes