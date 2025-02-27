def all_left_right_truncatable_prime(tuple):
    temp = all_prime_generator(x)
    result = []
    for num in temp:
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result