def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [x.lower() for x in lst]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]) and len(lst[i]) >= 3:
                anagram_count += 1
    return anagram_count >= 22