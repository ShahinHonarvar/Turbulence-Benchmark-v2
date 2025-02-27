def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagram_count += len(anagrams[sorted_str])
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    return anagram_count <= 30