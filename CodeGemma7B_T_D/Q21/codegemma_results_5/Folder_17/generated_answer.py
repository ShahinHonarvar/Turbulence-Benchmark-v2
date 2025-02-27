def all_ints_div_by_num(num: list) -> list:
    """
    This function returns a list of integers from index 33 to 35 inclusive that are divisible by 91 in the provided list.
    """
    divisible_nums = []
    for i in range(33, 36):
        if num[i] % 91 == 0:
            divisible_nums.append(num[i])
    return divisible_nums or []