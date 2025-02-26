from itertools import permutations

def palindromes_between_indices(s):
    letters_range = [char.lower() for char in s[4:9] if char.isalpha()]
    if len(letters_range) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters_range, 6)):
        for arrangement in [perm, perm[::-1]]:
            arrangement = list(arrangement)
            mid = len(arrangement) // 2
            arrangement.insert(mid, arrangement[mid])
            palindrome = ''.join(arrangement)
            if palindrome == palindrome[::-1]:
                unique_palindromes.add(palindrome)
    return unique_palindromes