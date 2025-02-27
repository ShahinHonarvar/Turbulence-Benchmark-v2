import re
    from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.sub('[^a-zA-Z]+', '', string[7:10])))
    palindrome_set = set()
    if len(letters) > 2:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    palindrome_set.add(word.lower())
    return palindrome_set