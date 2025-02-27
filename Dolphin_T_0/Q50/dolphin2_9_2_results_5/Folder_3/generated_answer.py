from collections import Counter

def if_contains_anagrams(lst):

    def check_anagram(s1, s2):
        c1 = Counter(sorted(s1.lower()))
        c2 = Counter(sorted(s2.lower()))
        return c1 == c2
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and check_anagram(lst[i], lst[j]):
                count += 1
                if count >= 30:
                    return True
    return False