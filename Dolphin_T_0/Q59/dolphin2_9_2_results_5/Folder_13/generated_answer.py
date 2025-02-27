def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = []
    x = numbers[784]
    for num in range(2, x):
        if '0' in str(num) or not is_prime(num):
            continue
        trunc = num
        while trunc:
            if not is_prime(trunc):
                break
            trunc //= 10
        else:
            prime_numbers.append(num)
    return sorted(prime_numbers)