from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_count[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values() if count > 1))
    return anagram_pairs <= 289