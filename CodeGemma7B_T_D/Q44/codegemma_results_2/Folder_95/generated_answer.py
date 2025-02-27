def composite_nums_between_indices(num_list):
    """
    Takes a list of positive integers.
    Returns the set of all composite numbers in the given list that are between index 26 to index 52, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for i in range(26, 53):
        if num_list[i] > 1 and any((num_list[i] % j == 0 for j in range(2, int(num_list[i] ** 0.5) + 1))):
            composite_nums.add(num_list[i])
    return composite_nums