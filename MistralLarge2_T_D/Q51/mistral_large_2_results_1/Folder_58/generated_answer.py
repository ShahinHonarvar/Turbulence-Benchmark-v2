from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    count = 0
    for words in anagram_dict.values():
        pairs = len(words) * (len(words) - 1) // 2
        count += pairs
        if count > 60:
            return False
    return count <= 60