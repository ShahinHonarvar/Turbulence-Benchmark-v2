def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = {}
    for s in string_list:
        cleaned = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned) < 3:
            continue
        sorted_s = ''.join(sorted(cleaned))
        if sorted_s in seen:
            seen[sorted_s] += 1
            anagram_count += seen[sorted_s]
        else:
            seen[sorted_s] = 0
        if anagram_count > 86:
            return False
    return True