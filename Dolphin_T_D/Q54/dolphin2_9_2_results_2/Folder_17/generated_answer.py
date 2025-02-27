def all_right_truncatable_prime(numbers):

    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        num_str = str(n)
        while num_str:
            if not check_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    x = numbers[36]
    primes = [i for i in range(x) if check_prime(i) and check_truncatable(i)]
    return sorted(primes, reverse=True)