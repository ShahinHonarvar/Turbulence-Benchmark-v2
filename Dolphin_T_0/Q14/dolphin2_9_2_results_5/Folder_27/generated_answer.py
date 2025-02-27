def find_second_smallest_num(nums):
    try:
        if 25 <= len(nums) < 59:
            return sorted(nums)[1]
    except:
        return None