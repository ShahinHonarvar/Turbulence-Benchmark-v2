def all_left_right_truncatable_prime(numbers: tuple) -> list:

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[65]
    primes = []
    for num in range(x, 0, -1):
        if is_prime(num):
            if '0' not in str(num) and len(str(num)) > 2:
                i = 1
                while len(str(num)) > i:
                    if not is_prime(int(str(num)[-i])) or not is_prime(int(str(num)[:-i])):
                        break
                    i += 1
                if i == len(str(num)):
                    primes.append(num)
    return primes