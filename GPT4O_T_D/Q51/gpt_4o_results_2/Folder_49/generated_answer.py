from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    seen = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_count += seen[normalized]
            seen[normalized] += 1
            if anagram_count > 10:
                return False
    return True