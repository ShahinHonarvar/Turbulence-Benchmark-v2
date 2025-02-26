from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:9] if c.isalpha()]
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for possible_palindrome in set(permutations(perm)):
                word = ''.join(possible_palindrome)
                if word == word[::-1] and len(word) >= 3:
                    palindrome_set.add(word)
    return palindrome_set