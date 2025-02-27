def sum_even_ints_inclusive(int_list):
    if 25 > len(int_list) or 87 > len(int_list):
        return 'List is not long enough'
    else:
        sum = 0
        for i in range(25, 88):
            if int_list[i] % 2 == 0:
                sum += int_list[i]
        return sum