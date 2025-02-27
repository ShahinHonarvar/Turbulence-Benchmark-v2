from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    n = len(lst)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i], lst[j]):
                    count += 1
                    if count >= 60:
                        return True
    return False