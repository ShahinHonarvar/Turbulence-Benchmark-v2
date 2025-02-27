import collections
from math import factorial

def if_contains_anagrams(strings):
    count = 0
    for word in strings:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            count += collections.Counter(word)
    result = list((count // factorial(2)).values())
    return sum((result[i] == result[i + 1] and result[i] == 0 for i in range(len(result) - 1))) == 276