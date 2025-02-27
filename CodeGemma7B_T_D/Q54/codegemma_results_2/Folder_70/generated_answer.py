def all_right_truncatable_prime(args):
    x = args[433]
    prime_list = []
    for num in range(x - 1, 1 - 1, -1):
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            for k in range(len(str(num)) - 1):
                new_num = int(str(num)[:-k - 1])
                if not is_prime(new_num):
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)