import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[2:9])).lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(2, len(s) // 2 + 1):
        for combo in itertools.combinations_with_replacement(letters, r):
            palindrome = ''.join(combo) + ''.join(combo[::-1])
            if len(palindrome) >= 4 and all((palindrome.count(c) <= s.count(c) for c in palindrome)):
                palindromes.add(palindrome)
    return palindromes