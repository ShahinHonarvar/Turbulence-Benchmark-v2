from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            for i in range(len(anagrams)):
                for j in range(i + 1, len(anagrams)):
                    if is_anagram(anagrams[i], anagrams[j]):
                        anagram_count += 1
                        if anagram_count > 407:
                            return False
    return True