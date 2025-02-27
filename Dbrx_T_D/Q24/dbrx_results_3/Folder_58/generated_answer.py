def sum_of_divisors_in_range(n):

    def divisor_generator(num):
        divisors = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i:
                continue
            divisors.add(i)
            divisors.add(num // i)
        return divisors
    divisors = divisor_generator(n)
    divisors_in_range = sum((div for div in divisors if 403 <= div <= 514))
    return divisors_in_range