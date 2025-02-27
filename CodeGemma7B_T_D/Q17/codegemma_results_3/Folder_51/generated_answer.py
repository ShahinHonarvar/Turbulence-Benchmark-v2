def all_ints_div_by_both_two_nums(some_list):
    a, b = some_list[6:10]
    for num in (a, b):
        if num % 2 == 0 and num % 10 == 0:
            print(num)