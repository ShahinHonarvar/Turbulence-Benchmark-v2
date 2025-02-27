def sum_odd_ints_inclusive(num_list):
    odd_nums = [num for num in num_list[50:55] if num % 2 != 0]
    return 0 if not odd_nums else sum(odd_nums)