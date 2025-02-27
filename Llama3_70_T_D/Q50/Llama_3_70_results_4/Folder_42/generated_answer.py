def if_contains_anagrams(lst):
    anagram_count = 0
    str_len_count = {}
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in str_len_count:
            str_len_count[sorted_str].append(s)
        else:
            str_len_count[sorted_str] = [s]
    for anagrams in str_len_count.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 233