from collections import Counter

def if_contains_anagrams(str_list):
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = Counter(str_list[i].lower())
            str2 = Counter(str_list[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pairs.add((str_list[i], str_list[j]))
    return len(anagram_pairs) <= 366