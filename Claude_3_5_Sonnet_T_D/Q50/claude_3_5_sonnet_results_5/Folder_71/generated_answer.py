def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = {}
    for s in string_list:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            anagram_count += len(seen[sorted_s])
            seen[sorted_s].append(s)
        else:
            seen[sorted_s] = [s]
        if anagram_count >= 57:
            return True
    return False