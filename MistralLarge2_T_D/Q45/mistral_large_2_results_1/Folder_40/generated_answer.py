import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[4:10])).lower()
    chars = set(substring)
    if len(chars) < 4:
        return set()
    palindromes = set()
    for length in range(7, len(substring) + 1):
        for perm in itertools.permutations(chars, length // 2):
            palindrome = ''.join(perm + perm[-(length // 2 + length % 2):-1:-1])
            if all((palindrome.count(c) <= substring.count(c) for c in chars)):
                palindromes.add(palindrome)
    return palindromes