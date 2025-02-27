from heapq import nsmallest

def find_second_smallest_num(num_list):
    sorted_nums = sorted(num_list[10:101])
    if not sorted_nums:
        return None
    return sorted_nums[1]