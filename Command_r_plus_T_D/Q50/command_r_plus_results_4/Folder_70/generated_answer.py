def if_contains_anagrams(str_list: list[str]) -> bool:
    anagram_count = 0
    str_list_lower = [s.lower() for s in str_list]
    for i in range(len(str_list_lower)):
        for j in range(i + 1, len(str_list_lower)):
            if len(str_list_lower[i]) >= 3 and len(str_list_lower[j]) >= 3:
                if sorted(str_list_lower[i]) == sorted(str_list_lower[j]):
                    anagram_count += 1
                    if anagram_count >= 189:
                        return True
    return False