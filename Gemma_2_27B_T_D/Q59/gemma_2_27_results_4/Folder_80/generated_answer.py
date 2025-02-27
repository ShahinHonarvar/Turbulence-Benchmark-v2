def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(x, 1, -1):
        if '0' not in str(num):
            is_truncatable = True
            num_str = str(num)
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)