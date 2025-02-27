def composite_nums_between_indices(list):
    """
    Takes one argument, a list of positive integers.
    Returns the set of all composite numbers in the given list that are between index 686 to index 987, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    output = set()
    for num in list[686:988]:
        for i in range(2, num):
            if num % i == 0:
                output.add(num)
                break
    return output