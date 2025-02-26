from itertools import permutations

def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]
    letters = ''.join((char.lower() for char in string[:6] if char.isalpha()))
    if len(letters) < 4:
        return set()
    result = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            sorted_candidate = ''.join(sorted(candidate))
            for arrangement in set(permutations(list(sorted_candidate))):
                palindrome = ''.join(arrangement)
                if is_palindrome(palindrome) and len(palindrome) >= 4:
                    result.add(palindrome)
    return result