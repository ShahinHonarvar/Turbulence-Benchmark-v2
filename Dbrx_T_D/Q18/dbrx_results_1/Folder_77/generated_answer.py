def sum_ints_div_by_either_nums(nums):
    start_index = 828
    end_index = 932
    divisors = [-649, -461]
    total = 0
    for i in range(start_index, end_index + 1):
        if nums[i] % divisors[0] == 0 or nums[i] % divisors[1] == 0:
            total += nums[i]
    return total