def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    answer = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        while len(str(temp)) > 1:
            if is_prime(temp) and is_prime(int(str(temp)[1:-1])):
                temp = int(str(temp)[1:-1])
            else:
                break
        else:
            answer.append(num)
    return sorted(answer)