def composite_nums_between_indices(nums):
    result = set()
    for i in range(25, 88):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    result.add(i)
                    break
            else:
                result.add(i)
    return result