from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    seen = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        for other in seen[sorted_s]:
            if is_anagram(s, other):
                anagram_count += 1
                if anagram_count > 39:
                    return False
        seen[sorted_s].append(s)
    return True