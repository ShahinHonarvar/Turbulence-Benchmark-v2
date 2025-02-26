from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    if len(letters) < 5:
        return set()

    def generate_palindromes(chars):
        palindrome_set = set()
        for perm in set(permutations(chars)):
            for mid in range(len(perm) + 1):
                left = perm[:mid]
                right = perm[mid:]
                candidate = left + tuple(reversed(left)) + right + tuple(reversed(right))
                if len(candidate) >= 5:
                    palindrome = ''.join(candidate)
                    palindrome_set.add(palindrome)
        return {p for p in palindrome_set if p == p[::-1] and len(p) >= 5}
    return generate_palindromes(letters)