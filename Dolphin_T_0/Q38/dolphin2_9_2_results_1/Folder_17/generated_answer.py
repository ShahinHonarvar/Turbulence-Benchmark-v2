def find_subset_of_length_n(s):
    if len(s) < 76:
        return 0

    def dfs(current_set, remaining_elements):
        if len(current_set) == 76:
            return 1
        if len(remaining_elements) == 0:
            return 0
        result = 0
        result += dfs(current_set, remaining_elements[1:])
        result += dfs(tuple(list(current_set) + [remaining_elements[0]]), remaining_elements[1:])
        return result
    return dfs(tuple([]), list(s))