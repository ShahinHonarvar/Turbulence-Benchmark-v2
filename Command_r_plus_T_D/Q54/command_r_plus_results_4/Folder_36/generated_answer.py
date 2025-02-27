def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num: int) -> list[int]:
        primes = []
        for i in range(10):
            num_str = str(num)
            truncated_num = int(num_str[:-1]) if len(num_str) > 1 else 0
            if is_prime(truncated_num):
                primes.append(num)
                num = truncated_num
            else:
                break
        return primes
    primes_list = []
    for num in numbers:
        if num > 1:
            primes_list.extend(generate_right_truncatable_primes(num))
    return sorted(set(primes_list))