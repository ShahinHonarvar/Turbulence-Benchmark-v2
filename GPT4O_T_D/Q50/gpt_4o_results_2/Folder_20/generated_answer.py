from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        count += n * (n - 1) // 2
        if count >= 64:
            return True
    return False