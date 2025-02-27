from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word].append(word)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return sum((count * (count - 1) // 2 for count in anagram_counts if count >= 2)) <= 6