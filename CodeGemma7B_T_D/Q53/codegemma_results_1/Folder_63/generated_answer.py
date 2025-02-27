from itertools import combinations

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for combination in combinations(text, 37):
        word = ''.join(combination)
        if word == word[::-1] and word.isalpha():
            palindromes.add(word)
    return palindromes