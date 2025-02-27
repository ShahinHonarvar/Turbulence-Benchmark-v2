def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [x.lower() for x in lst]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]) and len(lst[i]) >= 3 and (lst[i] != lst[j]):
                anagram_count += 1
                if anagram_count >= 15:
                    return True
    return False