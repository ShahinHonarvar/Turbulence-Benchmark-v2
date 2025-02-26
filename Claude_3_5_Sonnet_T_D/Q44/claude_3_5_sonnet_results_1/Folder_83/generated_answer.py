def composite_nums_between_indices(numbers):
    result = set()
    for num in numbers[111:112]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    result.add(num)
                    break
    return result