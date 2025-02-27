def if_contains_anagrams(str_list):
    pairs_anagrams = {}
    pairs_thirty = {}
    str_list = [s.lower() for s in str_list]
    str_list.sort()
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                if len(str_list[i]) >= 3:
                    pairs_thirty.setdefault(str_list[i], 0)
                    pairs_thirty[str_list[i]] += 1
                pairs_anagrams.setdefault(str_list[i], 0)
                pairs_anagrams[str_list[i]] += 1
    return len(pairs_thirty) <= 38 or len(pairs_anagrams) <= 38