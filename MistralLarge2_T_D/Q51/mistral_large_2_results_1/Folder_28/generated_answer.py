from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    n = len(strings)
    anagram_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 78:
                    return False
    return True