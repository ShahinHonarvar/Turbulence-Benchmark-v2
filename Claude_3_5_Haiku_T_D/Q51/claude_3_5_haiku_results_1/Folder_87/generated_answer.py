from collections import defaultdict

def if_contains_anagrams(strings):

    def is_valid_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_count = 0
    seen = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        for prev_s in seen[sorted_s]:
            if is_valid_anagram(s, prev_s):
                anagram_count += 1
                if anagram_count > 392:
                    return False
        seen[sorted_s].append(s)
    return True