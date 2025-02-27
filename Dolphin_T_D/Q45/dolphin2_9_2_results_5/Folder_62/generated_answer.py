def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:9].lower()
    letters = set([c for c in s if c.isalpha()])
    if len(''.join(letters)) < 7:
        return set()
    combinations = set()
    for i in range(7, len(list(letters)) + 1):
        for comb in itertools.combinations(letters, i):
            for p in permutations(comb):
                word = ''.join(p)
                if is_palindrome(word):
                    combinations.add(word)
    return combinations