def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst[:10]:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums