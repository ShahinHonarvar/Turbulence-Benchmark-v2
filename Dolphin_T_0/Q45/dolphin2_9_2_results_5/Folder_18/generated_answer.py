def palindromes_between_indices(s):

    def is_palindrome(w):
        return w == w[::-1]
    letters = [x for x in s[1:7] if x.isalpha()]
    all_arrangements = set(map(''.join, itertools.product(*map(string.ascii_letters, map(list, letters)))))
    palindromes = {w: is_palindrome(w) for w in all_arrangements if len(w) >= 3 and w.lower() == w.lower()[::-1]}
    return set(filter(None, map(is_palindrome, all_arrangements)))