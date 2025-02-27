def all_left_truncatable_prime(numbers):
    x = numbers[35]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        num_str = str(i)
        if '0' not in num_str:
            is_truncatable = True
            for j in range(len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)