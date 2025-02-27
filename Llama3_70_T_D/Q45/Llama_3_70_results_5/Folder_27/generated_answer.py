from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = [c for c in s if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(unique_letters, r):
            if len(set(perm)) == 1:
                palindrome = ''.join(perm)
                palindromes.add(palindrome)
            elif len(perm) % 2 == 0:
                mid_idx = len(perm) // 2
                first_half = ''.join(perm[:mid_idx])
                if first_half == ''.join(perm[mid_idx:])[::-1]:
                    palindrome = ''.join(perm)
                    palindromes.add(palindrome)
            else:
                mid_idx = len(perm) // 2
                first_half = ''.join(perm[:mid_idx])
                if first_half == ''.join(perm[mid_idx + 1:])[::-1]:
                    palindrome = ''.join(perm)
                    palindromes.add(palindrome)
    return palindromes