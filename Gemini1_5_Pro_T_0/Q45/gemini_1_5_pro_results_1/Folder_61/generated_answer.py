from collections import Counter
  import string

def palindromes_between_indices(string):
    letters = string.lower()
    letters = letters[:8]
    letters_dict = Counter(letters)
    palindrome_set = set()
    for word in permutations_of_letters(letters_dict):
        word = ''.join(word)
        if len(word) >= 7 and is_palindrome(word):
            palindrome_set.add(word)
    return palindrome_set

def permutations_of_letters(letters_dict):
    if not letters_dict:
        yield []
    else:
        for letter in letters_dict:
            if letters_dict[letter] > 0:
                letters_dict[letter] -= 1
                for permutation in permutations_of_letters(letters_dict):
                    yield ([letter] + permutation)
                letters_dict[letter] += 1

def is_palindrome(word):
    return word == word[::-1]