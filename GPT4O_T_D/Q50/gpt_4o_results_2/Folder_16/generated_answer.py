from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_groups[key].append(word)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            count += n * (n - 1) // 2
            if count >= 155:
                return True
    return False