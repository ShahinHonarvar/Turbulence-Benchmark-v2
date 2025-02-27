from collections import defaultdict

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_count = 0
    anagram_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        anagram_count += n * (n - 1) // 2
        if anagram_count > 14:
            return False
    return True