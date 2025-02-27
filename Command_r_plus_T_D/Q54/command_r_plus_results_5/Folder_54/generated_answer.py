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
        if num < 2:
            continue
        if is_prime(num):
            temp_num = num
            while temp_num > 9:
                temp_num //= 10
                if not is_prime(temp_num):
                    break
            if temp_num > 1:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    x = numbers[88]
    return [num for num in right_truncatable_primes if num < x]