def all_left_right_truncatable_prime(int_tuple):

    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    x = int_tuple[55]
    result = []
    for num in range(x, 1, -1):
        if check_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                while len(num_str) > 2 and check_prime(int(num_str)):
                    num_str = num_str[1:-1]
                if len(num_str) == 2 or len(num_str) == 1:
                    result.append(num)
    result.sort(reverse=True)
    return result