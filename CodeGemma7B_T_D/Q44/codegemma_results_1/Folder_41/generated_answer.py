def composite_nums_between_indices(lst):
    return {num for num in lst[0:3] if not is_prime(num)}

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True