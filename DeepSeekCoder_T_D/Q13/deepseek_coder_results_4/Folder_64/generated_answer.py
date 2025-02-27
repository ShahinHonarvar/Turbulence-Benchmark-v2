def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    top_two = sorted(nums[:5], reverse=True)[:2]
    return top_two[1] if len(top_two) == 2 else None