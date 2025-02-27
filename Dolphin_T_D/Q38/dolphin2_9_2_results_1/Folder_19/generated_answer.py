def find_subset_of_length_n(set_of_elements):

    def all_subsets(s):
        if not s:
            return [[]]
        else:
            head, *tail = s
            subsets = all_subsets(tail)
            return subsets + [[head] + subset for subset in subsets]
    count = 0
    subsets = all_subsets(set_of_elements)
    for subset in subsets:
        if len(subset) == 13:
            count += 1
    return count