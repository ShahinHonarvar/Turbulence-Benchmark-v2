def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    valid_strs = [s for s in lst if len(s) >= 3]
    sorted_list = [sorted_str(s) for s in valid_strs]
    count = 0
    seen = set()
    for s in sorted_list:
        if s in seen:
            count += 1
        else:
            seen.add(s)
    return count <= 92