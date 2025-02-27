from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    indices = s[3:9]
    letters = [ch.lower() for ch in indices if ch.isalpha()]
    letter_set = set(letters)
    all_palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                all_palindromes.add(palindrome)
    return all_palindromes