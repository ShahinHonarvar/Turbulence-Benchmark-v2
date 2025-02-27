def all_right_truncatable_prime(numbers):
    x = numbers[429]

    def is_right_truncatable_prime(num):
        if num <= 1:
            return False
        for i in range(len(str(num))):
            if int(str(num)[:len(str(num)) - i]) % 2 == 0 and int(str(num)[:len(str(num)) - i]) != 2:
                return False
            if not all([int(str(num)[:len(str(num)) - i]) % j for j in range(3, int(int(str(num)[:len(str(num)) - i]) ** 0.5) + 1, 2)]):
                return False
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)