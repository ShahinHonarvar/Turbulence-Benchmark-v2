from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    refined_words = [word for word in words if len(word) >= 3]
    for word in refined_words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for group in anagram_dict.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 181