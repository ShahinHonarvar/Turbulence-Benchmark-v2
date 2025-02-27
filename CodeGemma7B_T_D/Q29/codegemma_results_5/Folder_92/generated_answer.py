def gcf_two_nums(num_list):
    factor = num_list[0]
    for i in range(1, len(num_list)):
        factor = gcf(factor, num_list[i])
    return factor

def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a