from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[4:9] if char.isalpha()))
    if len(letters) < 5:
        return set()

    def generate_palindromes(chars):
        palinds = set()
        for perm in set(permutations(chars)):
            for length in range(5, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = perm[start:start + length]
                    if len(candidate) >= 5:
                        palindrome = candidate[:length // 2] + (candidate[length // 2] if length % 2 == 1 else '') + candidate[:length // 2][::-1]
                        if len(set(candidate)) == len(candidate):
                            palinds.add(palindrome)
        return palinds
    return generate_palindromes(letters)