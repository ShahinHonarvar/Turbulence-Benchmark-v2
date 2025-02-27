def if_contains_anagrams(lst):
    anagram_count = 0
    str_set = set()
    for s in lst:
        s = s.lower()
        if len(s) >= 3 and ''.join(sorted(s)) not in str_set:
            for str_ in lst[lst.index(s) + 1:]:
                str_ = str_.lower()
                if len(str_) >= 3 and sorted(s) == sorted(str_):
                    anagram_count += 1
            str_set.add(''.join(sorted(s)))
    return anagram_count >= 123