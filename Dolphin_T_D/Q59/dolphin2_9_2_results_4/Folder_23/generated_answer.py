def all_left_truncatable_prime(numbers):

    def check(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = numbers[77]
    result = []
    for n in range(2, x):
        if check(n):
            number = n
            while len(str(number)) > 0:
                if not check(number):
                    break
                number = number // 10
            else:
                result.append(n)
    return sorted(result, reverse=True)