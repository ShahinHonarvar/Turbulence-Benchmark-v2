from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    count = 0
    for word_list in anagram_map.values():
        if len(word_list) > 1:
            count += len(word_list) * (len(word_list) - 1) // 2
            if count > 91:
                return False
    return True