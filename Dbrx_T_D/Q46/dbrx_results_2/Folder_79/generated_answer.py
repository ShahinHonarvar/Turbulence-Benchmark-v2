from math import gcd

def apply_gcd(numbers):
    return numbers.reduce(gcd)

def gcf_three_nums_indices(numbers, indices):
    selected_numbers = [numbers[i] for i in indices]
    return apply_gcd(selected_numbers)

def gcf_three_nums(numbers):
    return gcf_three_nums_indices(numbers, [16, 87, 95])