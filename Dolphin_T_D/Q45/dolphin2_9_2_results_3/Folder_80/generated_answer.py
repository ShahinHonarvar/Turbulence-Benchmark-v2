import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    subset = [ch for ch in s[3:9] if ch.isalpha()]
    palindromes = set()
    for length in range(7, len(subset) + 1):
        for subset_part in itertools.combinations(subset, length):
            for p in itertools.permutations(subset_part):
                palindrome = ''.join(p).lower()
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes