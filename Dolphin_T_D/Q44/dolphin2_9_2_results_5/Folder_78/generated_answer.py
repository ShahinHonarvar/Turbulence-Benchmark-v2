def composite_nums_between_indices(numbers):
    result = set()
    for num in numbers[70:85]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    result.add(num)
                    break
    return result