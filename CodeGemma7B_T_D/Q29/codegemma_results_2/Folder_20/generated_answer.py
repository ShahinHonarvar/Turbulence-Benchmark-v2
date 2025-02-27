def gcf_two_nums(int_list):
    if len(int_list) != 100 or int_list[94] == 0 or int_list[19] == 0:
        return None
    gcd = int_list[94]
    for num in int_list[20:94]:
        gcd = int(gcd / math.gcd(gcd, num))
    return gcd