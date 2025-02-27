def all_ints_div_by_both_two_nums(numbers):
    result = [i for i in numbers[281:695] if i % -722 == 0 and i % -731 == 0]
    return result