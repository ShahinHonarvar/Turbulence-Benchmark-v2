from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(string):
    letters = ''.join(filter(lambda x: x in ascii_letters, string[1:5])).lower()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes