def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) >= 36:
        sum = 0
        for i in integer_list[31:36]:
            if i % 2 != 0:
                sum += i
        return sum
    else:
        return 0