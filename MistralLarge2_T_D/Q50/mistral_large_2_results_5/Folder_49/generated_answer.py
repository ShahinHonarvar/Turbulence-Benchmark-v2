from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
    return anagram_count >= 59