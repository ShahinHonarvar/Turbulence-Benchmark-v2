def sum_of_divisors_in_range(n):
    if isinstance(n, int) and n > 0:
        result_sum = 0
        for i in range(2, 7):
            if n % i == 0:
                result_sum += i
        return result_sum
    else:
        return 0