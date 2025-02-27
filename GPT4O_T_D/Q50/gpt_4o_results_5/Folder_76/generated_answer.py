from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    count = 0
    for anagram_list in anagram_map.values():
        num_words = len(anagram_list)
        if num_words > 1:
            count += num_words * (num_words - 1) // 2
            if count >= 143:
                return True
    return False