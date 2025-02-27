def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for num in range(numbers[31]):
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
        if is_prime(num) and is_prime(temp_num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)