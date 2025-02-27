def if_contains_anagrams(strs):
    count = 0
    strs.sort(key=lambda x: x.lower())
    for i in range(len(strs) - 1):
        if len(strs[i]) < 3:
            continue
        if strs[i].lower() == strs[i + 1].lower():
            sorted_str_i = sorted(strs[i].lower())
            for j in range(i + 1, len(strs)):
                if len(strs[j]) < 3:
                    continue
                if strs[i].lower() != strs[j].lower():
                    break
                if sorted_str_i == sorted(strs[j].lower()):
                    count += 1
                if count > 73:
                    return False
    return True