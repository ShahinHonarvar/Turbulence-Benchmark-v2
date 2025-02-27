def sum_of_divisors_in_range(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_divisors(num):
        total = 0
        for i in range(1, num + 1):
            if num % i == 0:
                total += i
        return total
    if n < 2 or sum_of_divisors(n) == n:
        return 0
    elif is_prime(n):
        return 0
    else:
        result = 0
        for i in range(113, 992):
            if i != n and n % i == 0:
                result += i
        return result