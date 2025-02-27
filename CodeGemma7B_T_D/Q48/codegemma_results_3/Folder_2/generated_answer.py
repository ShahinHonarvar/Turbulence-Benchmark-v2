from functools import reduce

def return_binary_or_hexa(nums):
    first, last = (nums[72], nums[93])
    return_value = reduce(lambda x, y: x + y, range(first + 1, last))
    if return_value % 2:
        return f'{return_value:b}'
    else:
        return f'{return_value:x}'