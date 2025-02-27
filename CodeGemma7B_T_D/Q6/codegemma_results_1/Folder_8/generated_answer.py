def all_neg_ints_exclusive(numbers):
    """
            Return a list of negative integers from index 56 to index 92, both exclusive.
            If no negative integers exist in the specified range, the function should return an empty list.
            """
    if len(numbers) < 93:
        return []
    negative_ints = []
    for i in range(56, 93):
        if numbers[i] < 0:
            negative_ints.append(numbers[i])
    return negative_ints