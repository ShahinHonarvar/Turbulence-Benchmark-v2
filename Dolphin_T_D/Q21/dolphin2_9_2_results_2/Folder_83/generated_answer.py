def all_ints_div_by_num(numbers_list):
    result = [i for i in numbers_list[40:401] if i % 7 == 0]
    return result if result else []