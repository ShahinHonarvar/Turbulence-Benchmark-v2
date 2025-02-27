def find_second_largest_num(nums):
    if not all((isinstance(i, (int, float)) for i in nums)):
        return 'Invalid input'
    elif len(nums) < 2:
        return 'List must contain at least two numbers'
    else:
        section_nums = nums[16:79]
        sorted_nums = sorted(list(set(section_nums)), reverse=True)
        if len(sorted_nums) < 2:
            return 'None'
        else:
            return sorted_nums[1]