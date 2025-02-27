def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[429]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 2:
                if num_str[0] == '0' or num_str[-1] == '0':
                    break
                if not is_prime(int(num_str[1:])) or not is_prime(int(num_str[:-1])):
                    break
                num_str = num_str[1:-1]
            else:
                primes.append(num)
    return sorted(primes, reverse=True) or []