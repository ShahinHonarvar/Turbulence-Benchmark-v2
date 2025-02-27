def find_subset_of_length_n(arr):

    def get_subsets(arr):
        if len(arr) == 0:
            return [[]]
        subsets = get_subsets(arr[1:])
        result = []
        for subset in subsets:
            result.append(subset)
            result.append([arr[0]] + subset)
            return result
    subsets = get_subsets(arr)
    length_n_subsets = [subset for subset in subsets if len(subset) == 360]
    return len(length_n_subsets)