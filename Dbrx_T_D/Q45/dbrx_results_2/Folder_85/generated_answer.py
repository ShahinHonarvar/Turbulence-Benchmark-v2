from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted(set(s.lower()[2:9]))
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes