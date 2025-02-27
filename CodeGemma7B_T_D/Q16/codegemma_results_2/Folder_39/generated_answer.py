def sum_even_ints_inclusive(num_list):
    nums = num_list[20:31]
    sum_of_evens = 0
    for num in nums:
        if num % 2 == 0:
            sum_of_evens += num
    if sum_of_evens == 0:
        return 0
    return sum_of_evens