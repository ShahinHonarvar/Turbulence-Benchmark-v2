def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for num in range(2, numbers[19]):
        truncated_num = num
        while truncated_num > 0:
            if not is_prime(truncated_num):
                break
            truncated_num //= 10
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)