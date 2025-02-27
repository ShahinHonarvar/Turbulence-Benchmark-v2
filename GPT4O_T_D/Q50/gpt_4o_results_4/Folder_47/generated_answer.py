from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 47:
            return True
    return False