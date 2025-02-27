from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    count = 0
    pair = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                count += 1
                pair.append((lst[i], lst[j]))
                if count > 21:
                    return False
    if count <= 21:
        return True
    return False