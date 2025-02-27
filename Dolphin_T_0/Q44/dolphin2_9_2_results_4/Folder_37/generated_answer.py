def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(0, 6):
        if not is_prime(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums