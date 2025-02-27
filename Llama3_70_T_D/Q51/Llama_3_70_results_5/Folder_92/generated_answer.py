def if_contains_anagrams(strings):
    count = 0
    anagram_dict = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            count += len(anagram_dict[sorted_s])
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    return count <= 34