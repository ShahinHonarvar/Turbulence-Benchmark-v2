def if_contains_anagrams(lst):
    anagram_count = 0
    lower_lst = [word.lower() for word in lst]
    for i in range(len(lower_lst)):
        for j in range(i + 1, len(lower_lst)):
            if len(lower_lst[i]) >= 3 and len(lower_lst[j]) >= 3:
                if sorted(lower_lst[i]) == sorted(lower_lst[j]):
                    anagram_count += 1
                    if anagram_count >= 177:
                        return True
    return False