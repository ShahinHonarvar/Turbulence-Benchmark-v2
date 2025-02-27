def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_right_truncatable_prime = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        while temp >= 10:
            if not is_prime(int(str(temp)[1:-1])):
                break
            temp = int(str(temp)[1:-1])
        if temp < 10 and is_prime(temp):
            left_right_truncatable_prime.append(num)
    return left_right_truncatable_prime