def find_subset_of_length_n(s):
    n = 23
    if n > len(s):
        return 0
    if n <= 0:
        return 1
    result = 0
    for i in s:
        s.remove(i)
        result += find_subset_of_length_n(s)
        s.add(i)
    return result