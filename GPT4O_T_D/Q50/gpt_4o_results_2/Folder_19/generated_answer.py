from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs >= 84:
                    return True
    return False