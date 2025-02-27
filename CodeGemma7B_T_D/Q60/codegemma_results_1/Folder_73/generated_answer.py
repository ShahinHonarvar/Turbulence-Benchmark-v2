def all_left_right_truncatable_prime(x):
    y = sorted([num for num in range(2, x + 1) if num % 2 != 0 and '0' not in str(num)])
    return result