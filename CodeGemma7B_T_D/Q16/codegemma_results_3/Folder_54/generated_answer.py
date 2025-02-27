def sum_even_ints_inclusive(list):
    sum = 0
    for number in list[34:56]:
        if number % 2 == 0:
            sum += number
    return sum if sum else 0