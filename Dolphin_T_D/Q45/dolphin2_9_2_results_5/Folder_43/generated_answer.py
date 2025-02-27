def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    subset = set(s[2:6])
    palindromes = set()
    for i in range(4, len(s[2:6]) + 1):
        for subset_sample in itertools.combinations(subset, i):
            for arrangement in itertools.permutations(''.join(sorted(subset_sample))):
                palindrome = ''.join(arrangement)
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes