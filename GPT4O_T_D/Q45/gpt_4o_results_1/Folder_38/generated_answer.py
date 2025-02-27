from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = ''.join(filter(str.isalpha, s[3:9]))
    palindromes = set()
    for perm in permutations(substring):
        potential_palindrome = ''.join(perm)
        if potential_palindrome == potential_palindrome[::-1] and len(potential_palindrome) >= 5:
            palindromes.add(potential_palindrome)
    return palindromes