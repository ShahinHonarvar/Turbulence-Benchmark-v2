def all_left_right_truncatable_prime(x):
    prime = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            num_str = str(num)
            if all((int(num_str[i:j]) != 0 and int(num_str[i:j]) != 1 for i in range(1, len(num_str) - 1) for j in range(i + 2, len(num_str) + 1))):
                for i in range(1, len(num_str) // 2 + 1):
                    if int(num_str[i:num_str.rindex(str(num_str[i]))]) not in prime:
                        break
                else:
                    prime.append(num)
    return sorted(prime, reverse=True)