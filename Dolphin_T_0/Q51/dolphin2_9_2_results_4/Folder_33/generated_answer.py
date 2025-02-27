from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return Counter(s1) == Counter(s2)
    count = 0
    n = len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 85:
                    return False
    return count >= 85