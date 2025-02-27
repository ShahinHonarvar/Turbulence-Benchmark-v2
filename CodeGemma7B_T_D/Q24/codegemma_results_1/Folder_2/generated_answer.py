def sum_of_divisors_in_range(number):
    answer = 0
    for divisor in range(315, 956):
        if number % divisor == 0:
            answer += divisor
    if answer == 0:
        return 0
    else:
        return answer