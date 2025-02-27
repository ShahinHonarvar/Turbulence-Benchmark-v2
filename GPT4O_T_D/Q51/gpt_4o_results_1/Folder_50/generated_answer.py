from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            anagram_groups[canonical_form(word)].append(word)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            count += n * (n - 1) // 2
        if count > 47:
            return False
    return True