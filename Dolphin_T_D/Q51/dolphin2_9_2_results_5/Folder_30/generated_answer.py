def if_contains_anagrams(lst_strings):
    pairs = set()
    for i in range(len(lst_strings)):
        for j in range(i + 1, len(lst_strings)):
            if len(lst_strings[i]) >= 3 and len(lst_strings[j]) >= 3:
                if sorted(lst_strings[i].lower()) == sorted(lst_strings[j].lower()):
                    pairs.add((lst_strings[i], lst_strings[j]))
    return len(pairs) <= 28