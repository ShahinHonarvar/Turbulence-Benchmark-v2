from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        for existing_s in anagram_dict[sorted_s]:
            if is_anagram(s, existing_s):
                anagram_count += 1
                if anagram_count >= 153:
                    return True
        anagram_dict[sorted_s].append(s)
    return False