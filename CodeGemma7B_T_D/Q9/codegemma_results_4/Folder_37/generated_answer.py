def all_odd_ints_inclusive(nums):
    output = []
    for i in range(1, 6):
        if i % 2 != 0:
            output.append(i)
    return output