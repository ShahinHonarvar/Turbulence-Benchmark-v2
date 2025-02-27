from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_string(word)
            anagram_groups[sorted_word].append(word)
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 136:
                return True
    return False