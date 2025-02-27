def sum_of_divisors_in_range(n):

    def get_divisors(num):
        return [i for i in range(11, 42) if num % i == 0]
    return sum(get_divisors(n))