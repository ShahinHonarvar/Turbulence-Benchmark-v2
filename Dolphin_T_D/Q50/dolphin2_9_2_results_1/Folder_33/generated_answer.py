from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for per in permutations(word):
                anagram = ''.join(per)
                if anagram != word:
                    counter = Counter(word.lower())
                    counter_anagram = Counter(anagram.lower())
                    if counter == counter_anagram:
                        count += 1
    return count >= 140