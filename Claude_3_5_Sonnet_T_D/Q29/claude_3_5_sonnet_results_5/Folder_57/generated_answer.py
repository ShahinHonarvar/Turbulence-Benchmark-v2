def gcf_two_nums(num_list):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(num_list) > 49 and isinstance(num_list[28], int) and isinstance(num_list[49], int):
        return calculate_gcf(num_list[28], num_list[49])
    else:
        return None