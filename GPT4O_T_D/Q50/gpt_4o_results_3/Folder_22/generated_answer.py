from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    count = 0
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            n = len(word_list)
            count += n * (n - 1) // 2
            if count >= 72:
                return True
    return False