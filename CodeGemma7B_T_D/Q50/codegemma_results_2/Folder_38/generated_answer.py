def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    pairs = [(s, t) for i, s in enumerate(str_list) for j, t in enumerate(str_list[i + 1:]) if sorted(s) == sorted(t) and len(s) >= 3]
    return len(pairs) >= 24