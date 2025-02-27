from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    anagram_pairs = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs.append((strings[i], strings[j]))
                if len(anagram_pairs) > 116:
                    return False
    return True