from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = set(string[0:4].lower()) & set('abcdefghijklmnopqrstuvwxyz')
    counts = Counter(string[0:4].lower())
    output = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                flag = True
                for letter in set(word):
                    if counts[letter] < word.count(letter):
                        flag = False
                if flag:
                    output.add(word)
    return output