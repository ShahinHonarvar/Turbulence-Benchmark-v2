def gcf_two_nums(num_list):
    if num_list[83] > num_list[14]:
        gcd = num_list[83]
    else:
        gcd = num_list[14]
    while num_list[83] % gcd != 0 or num_list[14] % gcd != 0:
        gcd -= 1
    return gcd