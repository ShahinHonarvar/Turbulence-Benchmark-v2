def composite_nums_between_indices(num_list):
    """
    Returns the set of composite numbers in a list between two indices, both inclusive.

    Args:
        num_list: A list of positive integers.

    Returns:
        A set of composite numbers between index 5 to index 5, both inclusive. If no such numbers exist, returns an empty set.
    """
    composite_nums = set()
    for i in range(5, 5 + 1):
        if num_list[i] % 2 == 0:
            composite_nums.add(num_list[i])
        for j in range(3, int(num_list[i] ** 0.5) + 1, 2):
            if num_list[i] % j == 0:
                composite_nums.add(num_list[i])
                break
    return composite_nums