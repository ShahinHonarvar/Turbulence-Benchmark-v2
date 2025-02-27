import math

def find_n_th_smallest_num(numbers):
    if len(numbers) <= 8:
        return sorted(numbers[2:])[6]
    else:
        sub_numbers = numbers[2:9]
        return sorted(sub_numbers)[6]