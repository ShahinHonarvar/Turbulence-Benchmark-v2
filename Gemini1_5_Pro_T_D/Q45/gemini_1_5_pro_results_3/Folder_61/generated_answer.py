from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[0:8].lower())
    keys = ''.join(letters.keys())
    palindromes = set()
    for i in range(len(keys) + 1):
        for perm in permutations(keys, i):
            word = ''.join(perm)
            if len(word) >= 7 and word == word[::-1]:
                flag = True
                for letter, count in Counter(word).items():
                    if letters[letter] < count:
                        flag = False
                if flag:
                    palindromes.add(word)
    return palindromes