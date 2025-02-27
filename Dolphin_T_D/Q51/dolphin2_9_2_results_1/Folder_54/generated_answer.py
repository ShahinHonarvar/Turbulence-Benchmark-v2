from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s, t):
        return sorted(s.lower()) == sorted(t.lower())
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                count += 1
                if count > 39:
                    return False
    return count <= 39