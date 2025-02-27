def all_odd_ints_inclusive(numbers):
    if len(numbers) < 52:
        return []
    odd_ints = []
    for i in range(26, 53):
        num = numbers[i]
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints