from functools import cmp_to_key

def find_n_th_smallest_num(num_list):

    def custom_sort(num1, num2):
        return num1 - num2
    sorted_nums = sorted(num_list[2:9], key=cmp_to_key(custom_sort))
    return sorted_nums[4]