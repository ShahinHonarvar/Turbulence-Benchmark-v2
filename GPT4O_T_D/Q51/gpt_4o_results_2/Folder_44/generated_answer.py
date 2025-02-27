from collections import defaultdict

def if_contains_anagrams(string_list):

    def sorted_string(s):
        return ''.join(sorted(s))
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            filtered_word = ''.join(filter(str.isalpha, word))
            key = sorted_string(filtered_word.lower())
            anagram_groups[key].append(filtered_word)
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 75