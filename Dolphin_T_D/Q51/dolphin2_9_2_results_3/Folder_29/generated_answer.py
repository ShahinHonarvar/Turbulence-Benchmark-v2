def if_contains_anagrams(lst):
    anagram_count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_count += 1
    if anagram_count <= 318:
        return True
    else:
        return False