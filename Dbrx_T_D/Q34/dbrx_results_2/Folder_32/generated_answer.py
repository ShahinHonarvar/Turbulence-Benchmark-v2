def find_max_diff(groups, k, max_diff):
    if k == 1:
        return max_diff
    max_possible_diff = max_diff
    for i in range(len(groups) - k + 1):
        current_sublist = groups[i:i + k]
        current_max_diff = max((max(sublist) - min(sublist) for sublist in current_sublist))
        max_possible_diff = max(max_possible_diff, current_max_diff)
    return max_possible_diff if max_possible_diff <= max_diff else -1