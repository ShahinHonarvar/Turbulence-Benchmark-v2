def composite_nums_between_indices(nums):
    for i in range(70, 85):
        if len(factors(i)) > 2:
            nums.append(i)
    return set(nums)

def factors(n):
    if n == 1:
        return [n]
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return sorted(factors)