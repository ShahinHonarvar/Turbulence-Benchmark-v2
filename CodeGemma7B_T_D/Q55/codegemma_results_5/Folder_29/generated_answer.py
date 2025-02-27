from itertools import islice

def lists_with_product_equal_n(nums):
    curr_list = []
    curr_product = 1
    result = []
    for num in itertools.cycle(nums):
        curr_list.append(num)
        curr_product *= num
        while curr_product > 15:
            curr_product //= curr_list.pop(0)
        if curr_product == 15:
            result.append(curr_list[:])
    return result