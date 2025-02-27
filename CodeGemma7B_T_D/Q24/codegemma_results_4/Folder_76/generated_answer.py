def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, 1000) if num % i == 0]
    filtered_divisors = [i for i in divisors if 744 <= i <= 885]
    return sum(filtered_divisors, 0)