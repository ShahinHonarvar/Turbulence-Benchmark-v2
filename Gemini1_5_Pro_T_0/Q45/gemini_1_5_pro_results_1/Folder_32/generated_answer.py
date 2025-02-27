from collections import Counter

def palindromes_between_indices(string):
    string = string[1:8].lower()
    letters = [letter for letter in string if letter.isalpha()]
    palindrome_set = set()
    if len(letters) < 5:
        return palindrome_set
    for i in range(5, len(letters) + 1):
        for combo in combinations_with_replacement(letters, i):
            word = ''.join(combo)
            if word[::-1] == word and word not in palindrome_set:
                palindrome_set.add(word)
    return palindrome_set