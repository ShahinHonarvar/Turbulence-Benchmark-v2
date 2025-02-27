from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    pairs = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return pairs <= 91