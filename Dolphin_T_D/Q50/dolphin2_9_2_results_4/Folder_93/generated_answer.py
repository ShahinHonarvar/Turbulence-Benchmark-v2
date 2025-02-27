def if_contains_anagrams(lst):
    if len(lst) < 36:
        return False
    lst_lower = [s.lower() for s in lst]
    count = sum((1 for s1, s2 in zip(lst_lower, lst_lower[1:]) if sort_string(s1) == sort_string(s2)))
    return count >= 18

def sort_string(s):
    return ''.join(sorted(s))