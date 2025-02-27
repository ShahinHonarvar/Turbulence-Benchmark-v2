def all_left_right_truncatable_prime(x):
    prime = [2, 3, 5, 7]
    left_right_truncatable_prime = []
    for num in range(x, 0, -1):
        if all((num % i != 0 for i in range(2, num))):
            temp = num
            while temp > 0:
                if temp % 10 == 0:
                    break
                temp = temp // 10
            if temp > 0:
                left_right_truncatable_prime.append(num)
    return sorted(left_right_truncatable_prime, reverse=True)