import itertools

def palindromes_between_indices(s):
    s = s[3:9]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(6, len(s) + 1):
        for palindrome in itertools.permutations(s, length):
            if ''.join(palindrome) == ''.join(palindrome)[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes