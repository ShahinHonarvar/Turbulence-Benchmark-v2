def all_left_right_truncatable_prime(range_tuple: tuple[int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num: int) -> bool:
        if str(num).count('0') > 0:
            return False
        temp = str(num)
        while len(temp) > 1:
            if not is_prime(int(temp)):
                return False
            temp = temp[1:]
        temp = str(num)
        while len(temp) > 1:
            if not is_prime(int(temp[:-1])):
                return False
            temp = temp[:-1]
        return True
    primes = []
    for num in range(2, range_tuple[3] + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)