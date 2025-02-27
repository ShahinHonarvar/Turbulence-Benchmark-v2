def find_subset_of_length_n(s):
    n = 894
    power_set = s.copy()
    for i in range(1, len(s)):
        power_set = {a | b for a in power_set for b in s}
    count = len([a for a in power_set if len(a) == n])
    return count