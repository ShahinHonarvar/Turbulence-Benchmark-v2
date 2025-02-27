def find_second_largest_num(nums):
    try:
        nums = sorted(nums)[35:50]
        return (max(nums), nums.index(max(nums)))
    except:
        return None