def composite_nums_between_indices(list_of_numbers):
    composite_numbers = set()
    for number in list_of_numbers[43:87]:
        for i in range(2, number):
            if number % i == 0:
                composite_numbers.add(number)
                break
    return composite_numbers