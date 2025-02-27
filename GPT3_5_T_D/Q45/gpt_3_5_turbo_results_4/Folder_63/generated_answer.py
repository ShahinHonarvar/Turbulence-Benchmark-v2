from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(string):
    string = string[:4].lower()
    if len(string) < 3:
        return set()
    palindromes = set()
    for permutation in permutations(string):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes