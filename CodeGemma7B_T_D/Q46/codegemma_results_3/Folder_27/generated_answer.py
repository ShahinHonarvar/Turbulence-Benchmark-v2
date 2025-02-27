def gcf_three_nums(num_list):
    num_one = num_list[76]
    num_two = num_list[64]
    num_three = num_list[28]
    return (math.gcd(num_one, num_two), math.gcd(num_two, num_three))