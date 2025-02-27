def composite_nums_between_indices(numbers):
    result = set()
    for number in numbers[82:87]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    result.add(number)
                    break
    return result