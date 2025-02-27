def if_contains_anagrams(lst):
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = ''.join(sorted(lst[i].lower()))
            str2 = ''.join(sorted(lst[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pairs.add(tuple(sorted([lst[i], lst[j]])))
    return len(anagram_pairs) >= 41