from math import sqrt

def composite_nums_between_indices(num_list):
    comp_nums = set()
    for i, num in enumerate(num_list):
        if i >= 5 and i <= 5 and (num_list[i] != 1):
            if num <= 2:
                continue
            elif num in [4, 6, 8, 9]:
                comp_nums.add(num)
            for j in range(3, int(sqrt(num)) + 1, 2):
                if num % j == 0:
                    comp_nums.add(num)
                    break
    return comp_nums