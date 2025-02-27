def sum_ints_div_by_either_nums(integers_list):
    specific_range = integers_list[7:10]
    divisible_by_either_nums = [i for i in specific_range if i % -9 == 0 or i % -7 == 0]
    return sum(divisible_by_either_nums) if divisible_by_either_nums else 0