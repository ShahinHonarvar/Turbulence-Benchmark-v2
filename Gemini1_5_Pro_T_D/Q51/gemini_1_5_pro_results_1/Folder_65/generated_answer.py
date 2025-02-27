import itertools
  from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i, j in itertools.combinations(list_of_strings, 2):
        if len(i) >= 3 and len(j) >= 3 and (Counter(i.lower()) == Counter(j.lower())):
            anagram_count += 1
    if anagram_count <= 72:
        return True
    else:
        return False