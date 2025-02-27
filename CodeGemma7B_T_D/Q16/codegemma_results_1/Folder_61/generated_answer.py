def sum_even_ints_inclusive(nums):
    sum_of_evens = 0
    for num in nums:
        if num % 2 == 0 and 0 <= nums.index(num) <= 7:
            sum_of_evens += num
    return sum_of_evens if sum_of_evens else 0