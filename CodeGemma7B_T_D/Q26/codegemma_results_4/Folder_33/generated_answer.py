def sum_in_range(num_list):
    """This function takes one argument, a list of integers,
            and returns the sum of all integers from the given list that are between 368 and 679, both inclusive.
            If the given list does not contain such integers, the function should return 0."""
    sum_of_nums = 0
    for num in num_list:
        if num >= 368 and num <= 679:
            sum_of_nums += num
    return sum_of_nums