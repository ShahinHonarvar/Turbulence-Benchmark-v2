def all_ints_div_by_num(nums):
    start = 255
    end = 618
    nums = [num for num in nums[start:end + 1] if num % 965 == 0]
    return nums