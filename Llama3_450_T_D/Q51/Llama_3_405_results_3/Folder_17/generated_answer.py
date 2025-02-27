def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s = s.lower()
        if len(s) < 3:
            continue
        if ''.join(sorted(s)) in anagram_dict:
            anagram_dict[''.join(sorted(s))].append(s)
        else:
            anagram_dict[''.join(sorted(s))] = [s]
    for v in anagram_dict.values():
        count += len(v) * (len(v) - 1) // 2
        if count > 22:
            return False
    return True