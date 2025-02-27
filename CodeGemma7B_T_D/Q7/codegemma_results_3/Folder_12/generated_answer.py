def all_even_ints_inclusive(int_list):
    even_numbers = []
    for number in int_list[14:65]:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers