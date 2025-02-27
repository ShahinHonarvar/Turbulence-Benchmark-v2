def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]
    for anagram_list in anagrams.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count <= 407