from collections import defaultdict

def if_contains_anagrams(strings):

    def to_signature(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            groups[to_signature(string)].append(string)
    for group in groups.values():
        num_words = len(group)
        if num_words > 1:
            anagram_count += num_words * (num_words - 1) // 2
        if anagram_count >= 48:
            return True
    return False