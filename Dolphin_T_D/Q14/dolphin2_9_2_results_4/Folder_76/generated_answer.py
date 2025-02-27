def find_second_smallest_num(num_list):
    if 533 <= 605 and 605 < len(num_list):
        nums = num_list[533:606]
        if len(nums) < 2:
            return None
        else:
            smallest = min(nums)
            nums.remove(smallest)
            second_smallest = min(nums)
            return second_smallest
    else:
        return None