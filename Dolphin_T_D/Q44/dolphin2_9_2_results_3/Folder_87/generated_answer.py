def composite_nums_between_indices(numbers):
    result = set()
    for i in range(43, 52):
        number = numbers[i]
        if number > 1:
            for x in range(2, number):
                if number % x == 0:
                    result.add(number)
                    break
    return result