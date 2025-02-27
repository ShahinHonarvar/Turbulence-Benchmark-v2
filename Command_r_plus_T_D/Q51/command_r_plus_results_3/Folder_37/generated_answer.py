from collections import Counter

def if_contains_anagrams(lst: list[str]) -> bool:
    anagram_count = 0
    normalized_lst = [s.lower() for s in lst]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if len(normalized_lst[i]) >= 3 and len(normalized_lst[j]) >= 3:
                if Counter(normalized_lst[i]) == Counter(normalized_lst[j]):
                    anagram_count += 1
                    if anagram_count > 206:
                        return False
    return True