def composite_nums_between_indices(nums):
    output = set()
    for i in range(69, 85):
        if all((num % i != 0 for i in range(2, num))):
            output.add(num)
    return output