def if_perfect_num(numbers):
    if len(numbers) < 685:
        return False
    index = 685
    number = numbers[index]
    sum_of_divisors = 0
    i = 1
    while i * i <= number:
        if number % i == 0:
            if_perfect_num_1 = i
            if number // i != i:
                if_perfect_num_2 = number // i
                sum_of_divisors += if_perfect_num_1 + if_perfect_num_2
            else:
                sum_of_divisors += if_perfect_num_1
        i += 1
    return sum_of_divisors == number