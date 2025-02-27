from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    for key in anagram_map:
        length = len(anagram_map[key])
        if length > 1:
            count += length * (length - 1) // 2
            if count >= 54:
                return True
    return False