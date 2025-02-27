def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = ''.join(sorted(lst[i].lower()))
            s2 = ''.join(sorted(lst[j].lower()))
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (s1 == s2):
                anagram_count += 1
    return anagram_count <= 20