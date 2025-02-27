from collections import defaultdict

def if_contains_anagrams(words):
    anagram_pairs = 0
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 401