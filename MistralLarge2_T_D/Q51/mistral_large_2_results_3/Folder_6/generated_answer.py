from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = set()
    string_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            string_dict[sorted_string].append(string)
    for group in string_dict.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if is_anagram(group[i], group[j]):
                        anagram_pairs.add((group[i], group[j]))
    return len(anagram_pairs) <= 86