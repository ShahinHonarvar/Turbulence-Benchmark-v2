def composite_nums_between_indices(num_list):

    def is_composite(n):
        return n > 1 and (n % 2 == 0 or n % 3 == 0 or (n % 2 != 0 and n % 3 != 0 and (n % 5 != 0)))
    result = set()
    for i in range(len(num_list)):
        if is_composite(num_list[i]) and i >= 111 and (i <= 222):
            result.add(num_list[i])
    return result