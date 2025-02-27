def find_original_set(*args):

    def is_subset(set1, set2):
        return all((elem in set1 for elem in set2))
    min_set = None
    for candidate_set in args:
        is_valid = True
        for other_set in args:
            if candidate_set != other_set and (not is_subset(candidate_set, other_set)):
                is_valid = False
                break
        if is_valid:
            if min_set is None or len(candidate_set) < len(min_set):
                min_set = candidate_set
    return min_set