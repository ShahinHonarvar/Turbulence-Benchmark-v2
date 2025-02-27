from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    count = 0
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 25