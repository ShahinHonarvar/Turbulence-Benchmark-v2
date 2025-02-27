def all_even_ints_inclusive(input_list):
    return [num for num in input_list if num % 2 == 0 and 0 <= input_list.index(num) <= 3]