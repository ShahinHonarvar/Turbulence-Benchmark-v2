def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    for v in anagram_dict.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
    return count <= 21