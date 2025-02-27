def if_contains_anagrams(str_list):
    anagrams = {}
    str_list = [''.join((c for c in s.lower() if c.isalnum())) for s in str_list]
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        anagrams.setdefault(sorted_s, []).append(s)
    return any((len(group) >= 86 for group in anagrams.values()))