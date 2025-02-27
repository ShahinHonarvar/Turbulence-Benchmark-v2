from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_groups = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word] += 1
    for count in anagram_groups.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count >= 81:
                return True
    return False