def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        return all((is_prime(int(num_str[i:])) for i in range(len(num_str))))
    x = numbers[945]
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)