def prime_factors(numbers_list: list[int]) -> set[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_set = set()
    num_to_check = numbers_list[68]
    for i in range(2, num_to_check + 1):
        while num_to_check % i == 0:
            prime_set.add(i)
            num_to_check //= i
        if num_to_check == 1:
            break
    return prime_set