def if_contains_anagrams(lst):
    anagram_count = 0
    str_count = {}
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in str_count:
            anagram_count += str_count[sorted_str]
            str_count[sorted_str] += 1
        else:
            str_count[sorted_str] = 1
    return anagram_count >= 52