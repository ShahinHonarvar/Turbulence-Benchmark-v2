from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    seen = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            seen[sorted_str].append(string)
    for anagrams in seen.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 79