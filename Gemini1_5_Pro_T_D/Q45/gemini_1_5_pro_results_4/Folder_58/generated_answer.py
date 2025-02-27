import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(0, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindrome_set = set()
    for i in range(6, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 6:
                palindrome_set.add(word)
    return palindrome_set