def if_contains_anagrams(lst):
    anagram_pairs = len([(a, b) for a in lst for b in lst if sorted(a.lower()) == sorted(b.lower()) and a != b and (len(a) >= 3) and (len(b) >= 3)])
    return anagram_pairs >= 20