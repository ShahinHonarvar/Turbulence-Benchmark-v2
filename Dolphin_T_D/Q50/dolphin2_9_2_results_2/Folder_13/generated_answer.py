def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst[i] = lst[i].lower()
                lst[j] = lst[j].lower()
                if sorted(lst[i]) == sorted(lst[j]) and lst[i] != lst[j]:
                    anagram_count += 1
                    if anagram_count >= 144:
                        return True
    return False