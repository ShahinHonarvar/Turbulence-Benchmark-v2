def composite_nums_between_indices(nums_list):

    def is_composite(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return True
        return False
    result = set()
    for num in nums_list[8:10]:
        if is_composite(num):
            result.add(num)
    return result