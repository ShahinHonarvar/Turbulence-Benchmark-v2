def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        leading_digits = [int(n[i:]) for i in range(len(str(n)) - 1)]
        return all(is_prime((int(str(n)[i:]) for i in range(len(str(n))))) and all((is_prime(x) for x in leading_digits)))
    x = numbers[19]
    output = []
    for num in range(2, x):
        if is_left_truncatable(num):
            output.append(num)
    return sorted(output)