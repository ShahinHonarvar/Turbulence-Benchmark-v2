import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[5:7] if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes