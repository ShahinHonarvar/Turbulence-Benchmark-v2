def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 64