def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[92]
    result = []
    for i in range(2, x + 1):
        if i < 10 and is_prime(i) or (i >= 10 and '0' not in str(i) and is_prime(i) and is_prime(int(str(i)[1:])) and is_prime(int(str(i)[:-1]))):
            result.append(i)
    return result