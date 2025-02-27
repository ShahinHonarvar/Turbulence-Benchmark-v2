def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = []
    for num in range(10, x):
        if is_prime(num):
            i = 0
            while num > 0:
                num = num // 10
                if is_prime(num):
                    i += 1
                else:
                    break
            if i > 0:
                prime_numbers.append(num)
    prime_numbers = sorted(prime_numbers, reverse=True)
    return prime_numbers