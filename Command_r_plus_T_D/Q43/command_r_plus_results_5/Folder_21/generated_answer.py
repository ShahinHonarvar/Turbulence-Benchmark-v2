def find_primes_between_indices(numbers_list: list[int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index, end_index = (478, 949)
    primes = [num for num in numbers_list[start_index:end_index + 1] if is_prime(num)]
    return sorted(primes, reverse=True)