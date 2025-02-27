def if_contains_anagrams(lst):
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    seen = set()
    anagram_count = 0
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            anagram_count += 1
        else:
            seen.add(sorted_s)
    return anagram_count <= 58