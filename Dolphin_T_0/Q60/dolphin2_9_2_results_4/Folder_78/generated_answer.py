def all_left_right_truncatable_prime(x):
    prime = [2]
    if x < 2:
        return []
    for num in range(3, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime.append(num)
    left_right_truncatable = []
    for num in prime:
        num_str = str(num)
        while num_str:
            if len(num_str) > 2:
                num_str = num_str[1:-1]
            if num_str == '':
                left_right_truncatable.append(num)
            elif int(num_str) not in prime:
                break
            elif len(num_str) == 1 and int(num_str) != num:
                break
    return left_right_truncatable