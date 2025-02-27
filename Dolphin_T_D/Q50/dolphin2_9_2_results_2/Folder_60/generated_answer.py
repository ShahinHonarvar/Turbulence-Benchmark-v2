def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = sum((is_anagram(w1, w2) for i in range(len(lst)) for j in range(i + 1, len(lst)) if len(lst[i]) >= 3 and len(lst[j]) >= 3))
    return anagram_pairs >= 60