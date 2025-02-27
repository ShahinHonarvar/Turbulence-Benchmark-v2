from functools import cmp_to_key

def find_second_largest_num(num_list):
    nums_sorted = sorted(num_list[75:89], key=cmp_to_key(lambda num1, num2: num2 - num1))
    return nums_sorted[-2] if len(nums_sorted) > 1 else None