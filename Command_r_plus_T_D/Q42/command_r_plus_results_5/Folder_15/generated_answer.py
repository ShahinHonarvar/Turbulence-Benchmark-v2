def prime_factors(numbers_list: list[int]) -> set[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_set = set()
    target_number = numbers_list[10]
    for i in range(2, target_number + 1):
        while target_number % i == 0:
            prime_set.add(i)
            target_number //= i
        if target_number == 1:
            break
    prime_set = {num for num in prime_set if is_prime(num)}
    return prime_set