from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1 and len(anagrams[0]) >= 3:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 70