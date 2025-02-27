def find_second_smallest_num(nums):
    filtered_nums = [num for i, num in enumerate(nums) if 90 <= i <= 200 and num != min(nums)]
    if len(filtered_nums) < 2:
        return None
    else:
        return sorted(filtered_nums)[1]