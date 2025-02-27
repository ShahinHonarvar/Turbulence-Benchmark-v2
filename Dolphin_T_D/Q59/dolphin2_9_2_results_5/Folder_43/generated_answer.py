def all_left_truncatable_prime(input_tuple):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = input_tuple[89]
    prime_list = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp = num
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
                if temp == 0:
                    prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list