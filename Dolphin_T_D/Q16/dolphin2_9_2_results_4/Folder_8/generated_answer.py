def sum_even_ints_inclusive(nums):
    sum = 0
    for number in nums:
        if 23 <= nums.index(number) <= 23 and number % 2 == 0:
            sum += number
    return sum or 0