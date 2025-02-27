def if_contains_anagrams(lst):
    anagram_count = sum((len([x for x in lst if sorted(x.lower()) == sorted(y.lower()) and len(x) >= 3]) for y in lst)) // 2
    return anagram_count <= 474