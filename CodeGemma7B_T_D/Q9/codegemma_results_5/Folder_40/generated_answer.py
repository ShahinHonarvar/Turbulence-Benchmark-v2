def all_odd_ints_inclusive(nums):
    result = []
    for num in range(3):
        if num % 2 != 0:
            result.append(num)
    return result