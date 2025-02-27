def find_primes_between_indices(numbers_list: list[int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index, end_index = (69, 84)
    primes = []
    for index in range(start_index, end_index + 1):
        if is_prime(numbers_list[index]):
            primes.append(numbers_list[index])
    return sorted(primes, reverse=True)