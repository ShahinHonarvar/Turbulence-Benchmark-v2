import itertools

def if_contains_anagrams(ls):
    ls = [s.lower() for s in ls if len(s) >= 3]
    anagrams = list(itertools.combinations(ls, 2))
    anagram_count = 0
    for anagram in anagrams:
        if sorted(anagram[0]) == sorted(anagram[1]):
            anagram_count += 1
    if anagram_count >= 47:
        return True
    else:
        return False