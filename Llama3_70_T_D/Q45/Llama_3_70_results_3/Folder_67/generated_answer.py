from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = ''.join(filter(str.isalpha, s[2:7]))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            if p[:i // 2] == p[:i - i // 2 - 1:-1]:
                palindrome = ''.join(p)
                palindromes.add(palindrome)
    return palindromes