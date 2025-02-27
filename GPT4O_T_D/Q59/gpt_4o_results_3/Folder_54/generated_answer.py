def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        str_num = str(num)
        return all((is_prime(int(str_num[i:])) for i in range(len(str_num))))
    x = numbers[88]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num) and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)