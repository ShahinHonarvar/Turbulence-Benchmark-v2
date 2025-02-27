def all_left_right_truncatable_prime(numbers):
    x = numbers[46]
    result = []
    for num in range(2, x + 1):
        if all([str(num).startswith(str(d)) is False for d in range(10)] + [str(num).endswith(str(d)) is False for d in range(10)]):
            str_num = str(num)
            if len(str_num) > 1 and all([int(str_num[:i]) in [2, 3, 5, 7] for i in range(1, len(str_num))]) and all([int(str_num[i:]) in [2, 3, 5, 7] for i in range(1, len(str_num))]):
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    result.append(num)
    result.sort(reverse=True)
    return result