def find_second_smallest_num(numbers):
    nums = numbers[1:9]
    if len(nums) < 2:
        return None
    return sorted(nums)[1]