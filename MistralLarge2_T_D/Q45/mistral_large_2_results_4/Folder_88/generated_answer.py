import itertools
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substr = ''.join(filter(str.isalpha, s[3:8].lower()))
    counter = Counter(substr)
    letters = ''.join(counter.elements())
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            if is_palindrome(''.join(combo)):
                palindromes.add(''.join(combo))
    return palindromes