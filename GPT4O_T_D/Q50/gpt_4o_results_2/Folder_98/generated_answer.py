from collections import defaultdict

def if_contains_anagrams(string_list):

    def sorted_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for word in string_list:
        if len(word) >= 3:
            sorted_word = sorted_form(word)
            anagram_count[sorted_word] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs >= 7