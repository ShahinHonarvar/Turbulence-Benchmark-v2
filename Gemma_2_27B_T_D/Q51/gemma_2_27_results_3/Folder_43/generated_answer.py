from collections import Counter

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagram_groups:
                anagram_groups[key].append(word)
            else:
                anagram_groups[key] = [word]
    count = sum((len(group) > 1 for group in anagram_groups.values()))
    return count <= 3