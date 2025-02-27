from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_groups[sorted_word].append(word)
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 22:
                return False
    return True