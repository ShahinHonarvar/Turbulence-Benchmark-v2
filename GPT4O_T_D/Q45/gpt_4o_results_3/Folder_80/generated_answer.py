from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    relevant_letters = [c for c in s[3:9] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for perm in permutations(relevant_letters):
        word = ''.join(perm)
        if len(word) >= 7 and is_palindrome(word):
            palindromes.add(word)
    return palindromes