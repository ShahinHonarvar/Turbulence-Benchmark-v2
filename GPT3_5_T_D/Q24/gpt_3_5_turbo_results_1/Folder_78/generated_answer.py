def sum_of_divisors_in_range(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0 and 20 <= i <= 50:
            divisors.append(i)
    return sum(divisors)