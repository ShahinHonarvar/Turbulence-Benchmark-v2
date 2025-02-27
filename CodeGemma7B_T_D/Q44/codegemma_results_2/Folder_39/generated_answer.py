def composite_nums_between_indices(lst):
    composite_nums = set()
    for idx, num in enumerate(lst):
        if 62 <= idx <= 92 and (not is_prime(num)):
            composite_nums.add(num)
    return composite_nums