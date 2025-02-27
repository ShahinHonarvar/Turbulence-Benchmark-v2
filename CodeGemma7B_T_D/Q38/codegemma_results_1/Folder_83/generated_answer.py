def find_subset_of_length_n(s, n):

    def powerset(s):
        if not s:
            return [[]]
        first = s[0]
        rest = s[1:]
        powerset_of_rest = powerset(rest)
        return powerset_of_rest + [[first] + s for s in powerset_of_rest]

    def count_subset(lst):
        if not lst:
            return 1
        return len(lst) * count_subset(lst[1:])
    return count_subset(powerset(s))