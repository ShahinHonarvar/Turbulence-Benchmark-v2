def composite_nums_between_indices(nums):
    composites = set()
    for idx, num in enumerate(nums):
        if idx >= 0 and idx <= 5:
            for divisor in range(2, round(num ** 1 / 2) + 1):
                if num % divisor == 0:
                    composites.add(num)
                    break
    return composites