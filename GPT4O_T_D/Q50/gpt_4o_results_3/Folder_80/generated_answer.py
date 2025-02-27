from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    count = 0
    for lst in anagram_dict.values():
        if len(lst) > 1:
            count += len(lst) * (len(lst) - 1) // 2
            if count >= 19:
                return True
    return False