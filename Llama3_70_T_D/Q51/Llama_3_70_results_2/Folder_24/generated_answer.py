def if_contains_anagrams(lst):
    pairs = 0
    anagrams = {}
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for anagram_list in anagrams.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs <= 96