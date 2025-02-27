def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                normalized_i = normalize_string(lst[i])
                normalized_j = normalize_string(lst[j])
                if normalized_i == normalized_j:
                    anagram_pair = tuple(sorted((lst[i], lst[j])))
                    if anagram_pair not in anagram_set:
                        anagram_set.add(anagram_pair)
                        anagram_count += 1
                    if anagram_count > 475:
                        return False
    return True