from collections import Counter

def if_contains_anagrams(strings_list):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    pairs = 0
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            if len(strings_list[i]) >= 3 and len(strings_list[j]) >= 3 and is_anagram(strings_list[i], strings_list[j]):
                pairs += 1
    return pairs >= 94