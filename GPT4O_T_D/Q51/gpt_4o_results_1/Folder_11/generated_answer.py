from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_count = 0
    seen = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_chars(s)
            seen[key] += 1
    for count in seen.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 41