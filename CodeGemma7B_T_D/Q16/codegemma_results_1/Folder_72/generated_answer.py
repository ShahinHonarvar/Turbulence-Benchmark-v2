def sum_even_ints_inclusive(int_list):
    total_sum = 0
    for number in int_list:
        if number % 2 == 0 and 29 <= index(number) <= 51:
            total_sum += number
    return total_sum if total_sum > 0 else 0