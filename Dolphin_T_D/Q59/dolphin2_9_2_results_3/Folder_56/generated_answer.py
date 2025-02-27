def all_left_truncatable_prime(args):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = args[30]
    result = [2]
    for num in range(3, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num)) - 1))) and is_prime(num):
            result.append(num)
    return sorted(result)