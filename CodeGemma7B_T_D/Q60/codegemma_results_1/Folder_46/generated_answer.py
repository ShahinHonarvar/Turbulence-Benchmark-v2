def all_left_right_truncatable_prime(x):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    for n in range(3, x + 1):
        if n not in prime:
            continue
        for num in str(n):
            if num == '0':
                break
            if n % int(num) != 0:
                break
        else:
            num_str = str(n)
            left = int(num_str[0])
            right = int(num_str[-1])
            while True:
                if len(num_str) < 2 or num_str == '1' or num_str == '2':
                    break
                if int(num_str) not in prime:
                    break
                left = int(num_str[0])
                right = int(num_str[-1])
                if left != right:
                    break
                num_str = num_str[1:-1]
            if len(num_str) < 2 or num_str == '1' or num_str == '2':
                result.append(n)
    result.sort()
    return result