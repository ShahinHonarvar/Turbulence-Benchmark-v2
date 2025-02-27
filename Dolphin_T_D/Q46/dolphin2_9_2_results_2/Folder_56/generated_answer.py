def gcf(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcf(a % b, b)
    return gcf(a, b % a)

def gcf_three_nums(num_list):
    gcf_59_93 = gcf(num_list[59], num_list[93])
    return gcf(gcf_59_93, num_list[84])