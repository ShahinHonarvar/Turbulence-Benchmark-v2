from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    words_lower = [word.lower() for word in words]
    anagram_groups = defaultdict(list)
    for word in words_lower:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 255:
                return False
    return True