def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    result = []
    for num in range(2, x + 1):
        if all((c != '0' for c in str(num))):
            is_truncatable_prime = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                left_truncation = int(str_num[i:])
                right_truncation = int(str_num[:-i])
                if not (left_truncation == 1 or left_truncation == 0 or right_truncation == 1 or (right_truncation == 0)):
                    if not (all((left_truncation % j for j in range(2, int(left_truncation ** 0.5) + 1))) and all((right_truncation % k for k in range(2, int(right_truncation ** 0.5) + 1)))):
                        is_truncatable_prime = False
                        break
                else:
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                if all((num % l for l in range(2, int(num ** 0.5) + 1))):
                    result.append(num)
    result.sort(reverse=True)
    return result