from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        count += n * (n - 1) // 2
        if count >= 34:
            return True
    return False