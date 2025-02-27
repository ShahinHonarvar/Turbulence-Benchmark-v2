def if_contains_anagrams(lst):
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                s1 = ''.join(filter(str.isalpha, lst[i].lower()))
                s2 = ''.join(filter(str.isalpha, lst[j].lower()))
                if sorted(s1) == sorted(s2):
                    anagram_pairs.add(tuple(sorted((lst[i], lst[j]))))
    return len(anagram_pairs) <= 277