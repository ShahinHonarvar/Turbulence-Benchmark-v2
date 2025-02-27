def composite_nums_between_indices(lst):
    comp_nums = []
    for i, num in enumerate(lst):
        if num > 1 and (not is_prime(num)):
            if i + 1 >= 1 and i + 1 <= len(lst) - 1:
                comp_nums.append(num)
    return set(comp_nums)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True