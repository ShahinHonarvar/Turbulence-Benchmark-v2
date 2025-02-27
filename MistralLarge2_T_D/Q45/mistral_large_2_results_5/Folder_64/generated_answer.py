import itertools

def palindromes_between_indices(s):
    char_set = set((c.lower() for c in s[4:10] if c.isalpha()))
    palindromes = set()
    for length in range(5, len(char_set) + 1):
        for p in itertools.permutations(char_set, length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes