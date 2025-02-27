def all_ints_not_div_by_num(nums):
    output = []
    for num in nums[60:200]:
        if num % 9 != 0:
            output.append(num)
    return output