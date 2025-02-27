def all_left_truncatable_prime(limit: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(current: int) -> list[int]:
        if current >= limit[54]:
            return []
        result = []
        for i in range(1, 10):
            new_num = current * 10 + i
            if is_prime(new_num):
                result.extend(generate_left_truncatable_primes(new_num))
        return [current] + result
    left_truncatable_primes = generate_left_truncatable_primes(2)
    left_truncatable_primes_under_x = [prime for prime in left_truncatable_primes if prime < limit[54]]
    return sorted(left_truncatable_primes_under_x)