def all_even_ints_exclusive(some_list):
    """
            Return a list of even integers from index 25 (inclusive) to index 80 (exclusive).
            If no even integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for number in some_list[25:80]:
        if number % 2 == 0:
            result.append(number)
    return result