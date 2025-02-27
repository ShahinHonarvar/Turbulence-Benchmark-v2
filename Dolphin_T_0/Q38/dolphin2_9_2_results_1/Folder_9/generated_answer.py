def find_subset_of_length_n(s):

    def find_subset(elements):
        if len(elements) == 24:
            return 1
        else:
            return sum((find_subset(elements + [x]) for x in s if x not in elements))
    return find_subset([])