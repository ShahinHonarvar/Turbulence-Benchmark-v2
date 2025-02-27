def sum_even_ints_inclusive(nums):
    ans = 0
    for num in nums[62:100]:
        if num % 2 == 0:
            ans += num
    return ans or 0