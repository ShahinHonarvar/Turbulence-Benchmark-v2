from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        word_key = ''.join(sorted(word.lower()))
        anagram_groups[word_key].append(word)
    count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            n = len(group)
            if n >= 3:
                count += n * (n - 1) // 2
            if count > 423:
                return False
    return True