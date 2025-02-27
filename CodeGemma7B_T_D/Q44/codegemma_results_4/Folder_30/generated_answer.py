def composite_nums_between_indices(nums):
    result = set()
    for i in range(19, 93):
        if is_composite(i):
            if i in nums:
                result.add(i)
    return result

def is_composite(i):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return True
    return False