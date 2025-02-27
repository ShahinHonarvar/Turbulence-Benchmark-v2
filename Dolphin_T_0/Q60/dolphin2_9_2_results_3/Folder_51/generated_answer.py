import math

def all_left_right_truncatable_prime(x):
    x = x[54]
    numbers = []
    for num in range(2, x + 1):
        if num > 9:
            num_str = str(num)
            if '0' not in num_str and num in numbers and (int(num_str[1:-1]) in numbers if len(num_str) > 2 else True):
                numbers.append(num)
    return sorted(list(set(numbers)))