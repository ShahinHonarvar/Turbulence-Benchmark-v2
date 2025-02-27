from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    count = 0
    word_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        word_map[sorted_word].append(word)
    for group in word_map.values():
        if len(group) >= 2 and len(group[0]) >= 3:
            count += len(group) * (len(group) - 1) // 2
    return count <= 41