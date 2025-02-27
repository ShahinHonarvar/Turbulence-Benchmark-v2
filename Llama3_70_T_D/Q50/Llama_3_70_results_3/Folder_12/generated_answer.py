def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [i.lower() for i in lst if len(i) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                anagram_count += 1
    return anagram_count >= 69