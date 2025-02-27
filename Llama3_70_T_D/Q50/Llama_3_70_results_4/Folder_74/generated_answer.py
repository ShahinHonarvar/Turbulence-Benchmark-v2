def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [''.join(sorted(s.casefold())) for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                anagram_count += 1
                if anagram_count >= 17:
                    return True
    return False