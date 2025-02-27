from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = defaultdict(int)
    for word in string_list:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        anagram_count[key] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_count >= 46