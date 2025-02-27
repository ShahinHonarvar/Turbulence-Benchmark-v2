from collections import defaultdict

def if_contains_anagrams(str_list):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1, str2 = (str_list[i], str_list[j])
            if len(str1) >= 3 and len(str2) >= 3 and are_anagrams(str1, str2):
                pair = tuple(sorted((i, j)))
                if pair not in checked_pairs:
                    anagram_count += 1
                    checked_pairs.add(pair)
    return anagram_count <= 36