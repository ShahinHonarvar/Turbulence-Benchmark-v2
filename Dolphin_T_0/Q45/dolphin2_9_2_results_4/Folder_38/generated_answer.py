import string
    from itertools import permutations

def palindromes_between_indices(string):
    permute_set = set()
    for i in range(3, 9):
        substring = string[i]
        permute_set.add(substring.lower())
    index = 0
    palindrome_set = set()
    while index < len(permute_set):
        palindrome = ''.join(permute_set)
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindrome_set.add(palindrome)
        index += 1
    return palindrome_set