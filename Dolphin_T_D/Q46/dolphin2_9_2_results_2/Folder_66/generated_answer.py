def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[92], num_list[69]), num_list[95])