import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(unique_letters, length):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes