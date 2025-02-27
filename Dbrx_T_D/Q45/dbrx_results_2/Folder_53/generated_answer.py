from collections import defaultdict
    from itertools import product

def palindromes_between_indices(s):
    chars = defaultdict(set)
    for i in range(4, 9):
        if i < len(s):
            chars[s[i].lower()].add(i)
    palindromes = set()
    for length in range(6, len(s) - 4 + 1):
        for indices in product(chars.keys(), repeat=length):
            palindrome = ''.join((s[i] for i in indices))
            if len(palindrome) == len(set(palindrome)) and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes