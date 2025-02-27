def find_second_smallest_num(nums):
    try:
        nums = sorted(nums)[30:88]
        return sorted(nums)[1]
    except IndexError:
        return None