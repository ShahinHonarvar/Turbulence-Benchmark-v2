def all_left_right_truncatable_prime(x):
    result = []
    for number in range(2, x + 1):
        flag = True
        if '0' in str(number):
            continue
        for i in range(1, len(str(number))):
            left = int(str(number)[:-i])
            right = int(str(number)[i:])
            if not (left == 1 or (left % 2 == 0 and left > 2) or left % 3 == 0 or (left % 5 == 0) or (left % 7 == 0)):
                flag = False
                break
            if not (right == 1 or (right % 2 == 0 and right > 2) or right % 3 == 0 or (right % 5 == 0) or (right % 7 == 0)):
                flag = False
                break
        if flag:
            result.append(number)
    return sorted(result, reverse=True)