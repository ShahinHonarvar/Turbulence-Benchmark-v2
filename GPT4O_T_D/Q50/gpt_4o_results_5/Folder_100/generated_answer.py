from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_map = defaultdict(int)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    anagram_count = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_count += sum(range(count))
    return anagram_count >= 95