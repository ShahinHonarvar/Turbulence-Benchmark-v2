from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    for key in anagram_map:
        n = len(anagram_map[key])
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 88:
                return True
    return False