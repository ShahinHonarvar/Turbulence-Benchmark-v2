from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 474:
                    return False
    return True