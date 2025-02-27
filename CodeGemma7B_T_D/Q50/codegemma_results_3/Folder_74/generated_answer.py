def if_contains_anagrams(str_list):
    str_list_lower = [s.lower() for s in str_list]
    str_list_lower.sort(key=len)
    anagram_count = 0
    for i, s in enumerate(str_list_lower):
        for j in range(i + 1, len(str_list_lower)):
            if sorted(s) == sorted(str_list_lower[j]) and len(s) >= 3:
                anagram_count += 1
    return anagram_count >= 17