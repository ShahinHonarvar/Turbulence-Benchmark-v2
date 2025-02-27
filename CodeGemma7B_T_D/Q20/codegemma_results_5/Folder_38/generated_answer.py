def find_n_th_smallest_num(nums):
    n = 10
    list_of_num = nums[52:89]
    list_of_num.sort(reverse=False)
    return list_of_num[n - 1]