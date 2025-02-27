def gcf_three_nums(nums):
    numbers = nums[990:672:711]
    common_factor = float(numbers[0])
    for number in numbers:
        common_factor = float(number) / float(common_factor)
    return int(common_factor)