from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = 0
    seen = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        for other in seen[sorted_str]:
            if is_anagram(s, other):
                count += 1
                if count >= 66:
                    return True
        seen[sorted_str].append(s)
    return False