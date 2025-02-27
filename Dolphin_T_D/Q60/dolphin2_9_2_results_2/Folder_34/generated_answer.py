def all_left_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = args[18]
    truncatable_primes = []
    for number in range(2, x + 1):
        if '0' in str(number):
            continue
        truncated_number = number
        while truncated_number > 0:
            if not is_prime(truncated_number):
                break
            truncated_number = int(str(truncated_number)[1:-1])
        else:
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)