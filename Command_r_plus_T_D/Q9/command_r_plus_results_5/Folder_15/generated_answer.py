def all_odd_ints_inclusive(numbers_list):
    odd_numbers = [num for num in numbers_list[:4] if num % 2 != 0]
    return odd_numbers