from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        str1 = ''.join(sorted(str1.lower()))
        str2 = ''.join(sorted(str2.lower()))
        return str1 == str2
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    count = 0
    for anagram_list in anagrams.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 85