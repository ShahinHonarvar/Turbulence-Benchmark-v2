def all_left_truncatable_prime(numbers):
    x = numbers[69]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or not all([int(str(n)[i:]) in (2, 3, 5, 7) or (int(str(n)[i:]) > 1 and all([int(str(n)[i:]) % j for j in range(2, int(int(str(n)[i:]) ** 0.5) + 1)])) for i in range(len(str(n)))]):
            return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)