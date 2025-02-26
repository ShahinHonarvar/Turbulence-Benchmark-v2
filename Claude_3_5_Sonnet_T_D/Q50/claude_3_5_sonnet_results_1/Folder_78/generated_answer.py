from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    anagram_count = 0
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count >= 79