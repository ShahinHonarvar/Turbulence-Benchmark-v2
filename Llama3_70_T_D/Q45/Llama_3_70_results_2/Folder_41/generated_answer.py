from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:4].lower()
    counter = Counter(s)
    palindromes = set()
    for r in range(3, sum(counter.values()) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                mid = len(word) // 2
                if len(word) % 2 == 0:
                    for i in range(mid):
                        if p[i] != p[-i - 1]:
                            break
                    else:
                        palindromes.add(word)
                else:
                    for i in range(mid):
                        if p[i] != p[-i - 1]:
                            break
                    else:
                        palindromes.add(word)
    return palindromes