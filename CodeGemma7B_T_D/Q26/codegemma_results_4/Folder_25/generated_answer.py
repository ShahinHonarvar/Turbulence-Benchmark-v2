def sum_in_range(num_list):
    """
            This function returns the sum of all integers from the given list
            that are between -10 and 48, both inclusive.

            Args:
                num_list: A list of integers.

            Returns:
                The sum of all integers from the given list that are between -10 and 48,
                both inclusive. If the given list does not contain such integers, the function
                should return 0.
            """
    sum = 0
    for num in num_list:
        if num >= -10 and num <= 48:
            sum += num
    return sum