from itertools import combinations_with_replacement

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[4:10].lower())
    palindromes = set()
    for letter in letters:
        for i in range(3, len(letters) + 1):
            for combo in combinations_with_replacement(letters, i):
                word = ''.join(combo)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes