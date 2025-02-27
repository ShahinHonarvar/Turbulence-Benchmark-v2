def all_left_truncatable_prime(numbers):
    x = numbers[945]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or not all([int(str(n)[i:]) in (2, 3, 5, 7) or (int(str(n)[i:]) % 2 and int(str(n)[i:]) % 3 and int(str(n)[i:]) % 5 and int(str(n)[i:]) % 7) for i in range(len(str(n)))]):
            return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)