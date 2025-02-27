def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return [j for j in divisors if j >= 43 and j <= 46]