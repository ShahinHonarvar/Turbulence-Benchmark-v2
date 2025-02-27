def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_str = normalize_string(lst[i])
        if len(normalized_str) < 3:
            continue
        for j in range(i + 1, len(lst)):
            other_normalized_str = normalize_string(lst[j])
            if len(other_normalized_str) < 3:
                continue
            if normalized_str == other_normalized_str:
                anagram_pair = tuple(sorted((lst[i], lst[j])))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 30:
                        return False
    return True