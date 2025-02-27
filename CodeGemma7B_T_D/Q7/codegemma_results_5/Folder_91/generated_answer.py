def all_even_ints_inclusive(int_list):
    even_numbers = []
    for num in int_list:
        if num % 2 == 0 and 0 <= num <= 5:
            even_numbers.append(num)
    return even_numbers