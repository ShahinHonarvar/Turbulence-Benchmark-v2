from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    anagram_pairs = 0
    for words in anagram_dict.values():
        if len(words) > 1:
            count = len(words)
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 84:
                return True
    return False