def composite_nums_between_indices(numbers):
    result = set()
    for i in range(1, min(len(numbers), 9)):
        if i < len(numbers) and i <= 8:
            num = numbers[i]
            if num > 1 and (not exact_sqrt(num)):
                result.add(num)
    return result

def exact_sqrt(n):
    return Math.sqrt(n) == int(Math.sqrt(n))