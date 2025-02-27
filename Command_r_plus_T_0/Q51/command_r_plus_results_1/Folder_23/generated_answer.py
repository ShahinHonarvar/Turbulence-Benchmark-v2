def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_str = normalize_string(lst[i])
        if len(normalized_str) >= 3 and normalized_str not in anagram_set:
            anagram_set.add(normalized_str)
            for j in range(i + 1, len(lst)):
                if normalize_string(lst[j]) == normalized_str:
                    anagram_count += 1
                    break
    return anagram_count <= 49