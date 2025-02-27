from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 60:
                return True
    return False