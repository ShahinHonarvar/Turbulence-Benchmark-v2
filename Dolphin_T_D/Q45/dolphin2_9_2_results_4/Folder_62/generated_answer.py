def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def combinations(s):
        if len(s) == 1:
            return [s]
        else:
            return [i + j for i in combinations(s[1:]) for j in combinations(s[:-1])]
    letters = [c for c in s[0:9] if c.isalpha()]
    letter_combinations = [[c for c in i if c in letters] for i in combinations(letters)]
    palindromes = []
    for i in letter_combinations:
        if len(i) >= 7 and is_palindrome(i):
            palindromes.append(i)
    return set(palindromes)