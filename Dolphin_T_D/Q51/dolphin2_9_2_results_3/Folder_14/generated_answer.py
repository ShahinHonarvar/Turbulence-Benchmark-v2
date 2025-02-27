def sorting_strings(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    result = {}
    for s in lst:
        if len(s) < 3:
            continue
        sorted_s = sorting_strings(s)
        if sorted_s in result:
            result[sorted_s] += 1
        else:
            result[sorted_s] = 1
    count = 0
    for key in result:
        count += result[key] * (result[key] - 1) // 2
    if count > 474:
        return False
    else:
        return True