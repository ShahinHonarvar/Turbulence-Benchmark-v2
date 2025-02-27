from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for group in anagram_dict.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
    return count <= 392