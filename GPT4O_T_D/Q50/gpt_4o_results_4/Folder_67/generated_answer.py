from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sort_string(string)
            anagram_dict[sorted_string].append(string)
    for words in anagram_dict.values():
        n = len(words)
        anagram_count += n * (n - 1) // 2
        if anagram_count >= 41:
            return True
    return False