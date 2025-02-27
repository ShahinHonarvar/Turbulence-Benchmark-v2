def find_subset_of_length_n(s):

    def powerset(s):
        result = [[]]
        for x in s:
            new_result = []
            for y in result:
                new_result.append(y + [x])
            result.extend(new_result)
        return result
    total_subsets = powerset(s)
    subset_size = [s for s in total_subsets if len(s) == 42]
    return len(subset_size)