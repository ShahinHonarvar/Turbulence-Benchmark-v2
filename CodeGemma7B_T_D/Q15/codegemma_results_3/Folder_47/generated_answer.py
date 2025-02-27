def sum_odd_ints_inclusive(num_list):
    result = 0
    for i in range(37, 77):
        if i % 2 != 0:
            result += num_list[i]
    return result
    print(sum_odd_ints_inclusive(num_list))
    print(0)