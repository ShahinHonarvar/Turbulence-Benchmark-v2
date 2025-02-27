from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            canonical = canonical_form(string)
            anagram_dict[canonical] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count >= 72:
                return True
    return False