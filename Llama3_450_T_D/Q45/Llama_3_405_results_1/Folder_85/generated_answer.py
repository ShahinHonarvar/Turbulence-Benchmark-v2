import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[2:9])).lower()
    letters = sorted(set(s))
    palindromes = set()
    for length in range(7, len(s) + 1):
        for combo in itertools.combinations(letters, length // 2):
            if length % 2 == 0:
                palindrome = ''.join(combo) + ''.join(combo[::-1])
            else:
                for letter in letters:
                    palindrome = ''.join(combo) + letter + ''.join(combo[::-1])
                    if palindrome in ''.join((p for p in itertools.permutations(s, length))):
                        palindromes.add(palindrome)
            if palindrome in ''.join((p for p in itertools.permutations(s, length))):
                palindromes.add(palindrome)
    return palindromes