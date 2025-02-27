def if_contains_anagrams(lst):

    def get_sorted_str(s):
        return ''.join(sorted(s.lower()))
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (get_sorted_str(lst[i]) == get_sorted_str(lst[j])):
                count += 1
            if count > 188:
                return False
    return count <= 188