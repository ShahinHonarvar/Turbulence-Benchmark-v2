def composite_nums_between_indices(input_list):
    return {num for num in input_list[25:60] if num > 1 and (not is_prime(num))}

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True