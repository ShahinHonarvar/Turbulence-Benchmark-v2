from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = defaultdict(list)
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_count.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs <= 97