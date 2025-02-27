def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                anagram_count += 1
    return anagram_count >= 48