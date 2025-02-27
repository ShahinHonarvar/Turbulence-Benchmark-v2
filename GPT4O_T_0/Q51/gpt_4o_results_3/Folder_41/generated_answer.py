from collections import defaultdict

def if_contains_anagrams(strings):

    def is_valid_anagram(s1, s2):
        return sorted(s1) == sorted(s2) and len(s1) >= 3 and (len(s2) >= 3)
    anagram_count = 0
    normalized_strings = [s.lower() for s in strings]
    anagram_dict = defaultdict(list)
    for s in normalized_strings:
        key = ''.join(sorted(s))
        anagram_dict[key].append(s)
    for key, group in anagram_dict.items():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if is_valid_anagram(group[i], group[j]):
                        anagram_count += 1
                        if anagram_count > 52:
                            return False
    return True