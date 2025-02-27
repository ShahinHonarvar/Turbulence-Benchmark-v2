from itertools import permutations

def palindromes_between_indices(s):
    relevant_chars = ''.join((c for c in s[:7] if c.isalpha())).lower()
    possible_palindromes = set()
    for length in range(6, len(relevant_chars) + 1):
        for perm in permutations(relevant_chars, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                possible_palindromes.add(palindrome)
    return possible_palindromes