def if_contains_anagrams(strs):
    anagram_sets = {}
    for str_ in strs:
        if not re.match('^[a-zA-Z]{3,}$', str_):
            continue
        str_lower = str_.lower()
        sorted_str = ''.join(sorted(str_lower))
        anagram_sets.setdefault(sorted_str, set()).add(str_lower)
    return len(anagram_sets) <= 181