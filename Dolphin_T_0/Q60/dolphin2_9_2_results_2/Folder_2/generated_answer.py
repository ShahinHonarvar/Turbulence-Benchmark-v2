def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[618]
    result = []
    for i in range(2, x):
        if is_prime(i) and i % 10 != 0:
            num = i
            while True:
                if not is_prime(num) or num == i:
                    break
                num = int(str(num)[1:-1])
                result.append(i)
    return sorted(list(set(result)))