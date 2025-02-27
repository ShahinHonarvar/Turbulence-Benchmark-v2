def find_second_smallest_num(numbers):
    nums = numbers[40:81]
    if not nums:
        return 'None'
    nums.sort()
    return nums[1]