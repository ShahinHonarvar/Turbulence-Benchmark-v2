def all_left_truncatable_prime(n):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = n[466]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp_num = num
            while temp_num > 1:
                if not is_prime(temp_num):
                    break
                temp_num //= 10
                if temp_num == 0:
                    result.append(num)
    return sorted(result, reverse=True)