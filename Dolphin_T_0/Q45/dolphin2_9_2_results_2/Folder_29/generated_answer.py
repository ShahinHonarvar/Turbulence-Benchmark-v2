import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s[2:10])).lower()
    palindrome_set = set()
    for i in range(6, len(s) + 1):
        for combination in itertools.combinations(s, i):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if is_palindrome(palindrome):
                    palindrome_set.add(palindrome)
    return palindrome_set