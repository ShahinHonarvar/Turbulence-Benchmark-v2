def find_n_th_smallest_num(nums):
    if len(nums) < 15:
        return None
    return sorted(nums[:15])[14]