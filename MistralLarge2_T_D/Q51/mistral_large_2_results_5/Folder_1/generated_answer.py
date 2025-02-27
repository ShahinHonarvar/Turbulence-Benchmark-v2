from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_dict = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    for key in anagram_dict:
        anagram_list = anagram_dict[key]
        if len(anagram_list) > 1:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
        if count > 30:
            return False
    return True