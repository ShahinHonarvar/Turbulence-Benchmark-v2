def all_right_truncatable_prime(x):
    prime = [2, 3, 5, 7]
    for num in range(11, x):
        for divide in range(2, int(num ** 0.5) + 1):
            if num % divide == 0:
                break
        else:
            prime.append(num)
    right_truncatable_prime = []
    for num in prime:
        str_num = str(num)
        for i in range(len(str_num) - 1):
            if int(str_num[i:]) not in prime:
                right_truncatable_prime.append(int(str_num[i:]))
                break
    return sorted(right_truncatable_prime, reverse=True)