def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(len(int_list)):
        if i >= 60 and i < 200:
            num = int_list[i]
            if num % 2 != 0:
                odd_ints.append(num)
    return odd_ints