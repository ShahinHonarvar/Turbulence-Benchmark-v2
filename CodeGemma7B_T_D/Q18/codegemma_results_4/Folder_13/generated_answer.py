def sum_ints_div_by_either_nums(num_list):
    """
    This function takes one argument, a list of integers, and returns the sum of all integers divisible by either 45 or 20 from index 13 to index 18, both inclusive. If no such integers exist in the specified range, the function should return 0.
    """
    sum_div_nums = []
    for num in num_list[13:19]:
        if num % 45 == 0 or num % 20 == 0:
            sum_div_nums.append(num)
    return sum(sum_div_nums) if sum_div_nums else 0