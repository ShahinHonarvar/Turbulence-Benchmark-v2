def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for num in numbers:
        if num >= x:
            break
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(num) or not is_prime(temp_num):
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)