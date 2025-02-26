def sum_ints_div_by_either_nums(integer_list):
    filtered_nums = [num for num in integer_list[80:201] if num % 10 == 0 or num % 1000 == 0]
    return sum(filtered_nums)