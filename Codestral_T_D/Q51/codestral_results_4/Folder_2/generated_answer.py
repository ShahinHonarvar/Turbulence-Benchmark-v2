from collections import defaultdict

def if_contains_anagrams(word_list):
    d = defaultdict(list)
    for word in word_list:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            d[key].append(word)
    anagram_count = sum((len(anagram_group) * (len(anagram_group) - 1) for anagram_group in d.values()))
    return anagram_count <= 81