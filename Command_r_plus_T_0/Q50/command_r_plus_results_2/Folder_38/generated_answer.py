def if_contains_anagrams(lst):
    anagram_count = 0
    normalized_lst = [word.lower() for word in lst]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if len(normalized_lst[i]) >= 3 and len(normalized_lst[j]) >= 3:
                if sorted(normalized_lst[i]) == sorted(normalized_lst[j]):
                    anagram_count += 1
                    if anagram_count >= 24:
                        return True
    return False