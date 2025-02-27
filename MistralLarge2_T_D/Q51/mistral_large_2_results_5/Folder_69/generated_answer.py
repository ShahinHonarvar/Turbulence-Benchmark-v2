from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    seen = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        for seen_str in seen[sorted_s]:
            if is_anagram(s, seen_str):
                anagram_count += 1
                if anagram_count > 58:
                    return False
        seen[sorted_s].append(s)
    return anagram_count <= 58