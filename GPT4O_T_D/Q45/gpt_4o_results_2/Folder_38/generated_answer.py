from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    relevant_substring = s[3:9].lower()
    letters_only = ''.join(filter(str.isalpha, relevant_substring))
    palindromes = set()
    for length in range(5, len(letters_only) + 1):
        for perm in permutations(letters_only, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes