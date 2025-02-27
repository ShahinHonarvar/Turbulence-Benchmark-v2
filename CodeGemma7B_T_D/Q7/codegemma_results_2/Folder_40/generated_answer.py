def all_even_ints_inclusive(int_list):
    even_nums = []
    for num in int_list:
        if num % 2 == 0 and num >= 0 and (num <= 2):
            even_nums.append(num)
    return even_nums