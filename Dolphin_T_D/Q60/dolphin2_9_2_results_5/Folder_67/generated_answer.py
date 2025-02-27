def all_left_right_truncatable_prime(x):
    prime = [2, 3, 5, 7]
    left_right_truncatable = []
    for num in range(3, int(x), 2):
        if num > 1:
            for i in prime:
                if num % i == 0:
                    break
            else:
                str_num = str(num)
                left_right_removal = str(int(str_num[1:-1]))
                if len(left_right_removal) > 0:
                    if set(left_right_removal).issubset(set(str(num))):
                        left_right_truncatable.append(num)
                        prime.append(num)
    left_right_truncatable.sort(reverse=True)
    return left_right_truncatable