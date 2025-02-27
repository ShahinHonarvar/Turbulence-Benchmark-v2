def find_subset_of_length_n(s):
    d = {}

    def find_subsets(n, string):
        if len(string) == n:
            d[string] = d.get(string, 0) + 1
            return
        for char in s:
            if string + char not in d:
                find_subsets(n, string + char)
    find_subsets(59, '')
    return len(d)