def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    pairs = 0
    for i, s in enumerate(str_list):
        for j in range(i + 1, len(str_list)):
            if sorted(s) == sorted(str_list[j]) and len(s) >= 3:
                pairs += 1
                if pairs >= 15:
                    return True
    return False