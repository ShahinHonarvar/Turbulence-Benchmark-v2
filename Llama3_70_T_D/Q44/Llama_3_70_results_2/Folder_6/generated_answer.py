def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(max(0, 13), min(68 + 1, len(lst))):
        num = lst[i]
        if not is_prime(num):
            composite_nums.add(num)
    return composite_nums