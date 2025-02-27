from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[sorted_string(word)].append(word)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 24:
                return True
    return False