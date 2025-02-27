from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    seen = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for seen_word in seen[sorted_word]:
            if is_anagram(word.lower(), seen_word.lower()):
                count += 1
                if count > 41:
                    return False
        seen[sorted_word].append(word)
    return True