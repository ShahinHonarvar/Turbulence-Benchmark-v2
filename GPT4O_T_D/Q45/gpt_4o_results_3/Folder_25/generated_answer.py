from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    sub_str = s[1:5]
    letters = [c for c in sub_str if c.isalpha()]
    if len(letters) < 3:
        return set()
    possible_palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in permutations(letters, length):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                possible_palindromes.add(candidate)
    return possible_palindromes