def all_odd_ints_inclusive(nums):
    output = []
    for i in range(62, 100):
        if i % 2 != 0:
            output.append(i)
    if len(output) == 0:
        output = []
    return output