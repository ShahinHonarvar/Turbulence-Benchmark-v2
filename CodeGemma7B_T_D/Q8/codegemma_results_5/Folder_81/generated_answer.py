def all_even_ints_exclusive(int_list):
    even_nums = []
    for num in int_list[10:100]:
        if num % 2 == 0 and num not in even_nums:
            even_nums.append(num)
    return even_nums