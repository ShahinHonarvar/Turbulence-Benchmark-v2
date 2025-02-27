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
            new_num = num * 10 + i
            if is_prime(new_num):
                primes.append(new_num)
        return primes
    limit = numbers[32]
    right_truncatable_primes = []
    for i in range(2, limit):
        if is_prime(i):
            temp_list = [i]
            for j in range(len(str(i)) - 1):
                temp_list = generate_right_truncatable_primes(temp_list[-1])
                if not temp_list:
                    break
            if temp_list:
                right_truncatable_primes.extend(temp_list)
    return sorted(set(right_truncatable_primes))