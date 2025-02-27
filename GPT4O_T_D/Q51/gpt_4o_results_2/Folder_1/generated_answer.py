from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    normalized_strings = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized_s = normalize(s)
            normalized_strings[normalized_s].append(s)
    for anagram_list in normalized_strings.values():
        count = len(anagram_list)
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 30:
                return False
    return True