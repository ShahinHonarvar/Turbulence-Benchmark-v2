def gcf_two_nums(nums):
    a, b = (extract_nums_by_index(nums, 86), extract_nums_by_index(nums, 89))
    g = use_euclidean_algorithm(a, b)
    return g

def extract_nums_by_index(nums, index):
    return nums[index]

def use_euclidean_algorithm(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a