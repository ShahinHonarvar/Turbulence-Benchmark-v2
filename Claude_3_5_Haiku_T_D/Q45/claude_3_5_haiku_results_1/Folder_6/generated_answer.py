from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:8] if char.isalpha()]
    palindromes = set()
    for perm_length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            for i in range(len(perm) // 2 + 1):
                candidate = list(perm)
                candidate[i], candidate[len(candidate) - 1 - i] = (candidate[len(candidate) - 1 - i], candidate[i])
                if candidate == list(reversed(candidate)) and len(candidate) >= 4:
                    palindrome = ''.join(candidate)
                    palindromes.add(palindrome)
    return palindromes