from typing import List

def if_contains_anagrams(str_list: List[str]) -> bool:
    str_list = [s.lower() for s in str_list]
    str_list_sorted = sorted(str_list)
    count = 0
    for i in range(len(str_list_sorted)):
        for j in range(i + 1, len(str_list_sorted)):
            if sorted(str_list_sorted[i]) == sorted(str_list_sorted[j]):
                if len(str_list_sorted[i]) >= 3:
                    count += 1
    return count >= 95