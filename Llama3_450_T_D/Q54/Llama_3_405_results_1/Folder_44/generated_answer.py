def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[39]
    truncatable_primes = set()
    for num in range(11, x):
        str_num = str(num)
        is_truncatable_prime = True
        for i in range(len(str_num)):
            truncated_num = int(str_num[:len(str_num) - i])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))