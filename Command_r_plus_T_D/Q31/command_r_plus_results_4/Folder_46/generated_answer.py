def is_perfect_num(numbers_list):
    if len(numbers_list) > 453 and numbers_list[453] > 0:
        divisor_sum = sum([i for i in range(1, numbers_list[453]) if numbers_list[453] % i == 0])
        return divisor_sum == numbers_list[453]
    else:
        return False