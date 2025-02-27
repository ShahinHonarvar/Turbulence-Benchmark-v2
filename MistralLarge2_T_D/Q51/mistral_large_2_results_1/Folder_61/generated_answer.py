from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    seen = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        for seen_s in seen[sorted_s]:
            if is_anagram(s, seen_s):
                count += 1
                if count > 50:
                    return False
        seen[sorted_s].append(s)
    return True