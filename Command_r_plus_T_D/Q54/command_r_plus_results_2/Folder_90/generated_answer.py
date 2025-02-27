def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for num in range(1, 10):
            if is_prime(num):
                primes.append(num)
        while primes:
            current_prime = primes[0]
            if current_prime < limit:
                for digit in range(1, 10):
                    new_num = current_prime * 10 + digit
                    if is_prime(new_num):
                        primes.append(new_num)
            primes.pop(0)
        return primes
    limit = numbers[466]
    primes = generate_right_truncatable_primes(limit)
    return sorted([prime for prime in primes if prime < limit], reverse=True)