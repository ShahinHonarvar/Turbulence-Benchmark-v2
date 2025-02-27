def find_second_smallest_num(num_list):
    try:
        nums = sorted(num_list[6:9])
        return nums[1]
    except IndexError:
        return None