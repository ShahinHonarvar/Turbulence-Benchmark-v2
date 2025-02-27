def all_left_right_truncatable_prime(nums):
    x = nums[7]
    possible_list = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for n in range(2, x + 1):
        if is_prime(n):
            str_n = str(n)
            if '0' in str_n:
                continue

            def is_truncatable(number):
                if len(str(number)) == 1:
                    return True
                if is_prime(number):
                    lead = str(number)
                    tail = str(number)
                    while len(lead) > 1:
                        lead = lead[:-1]
                        if not is_prime(int(lead)):
                            return False
                    while len(tail) > 1:
                        tail = tail[1:]
                        if not is_prime(int(tail)):
                            return False
                    return True
            if is_truncatable(n):
                possible_list.append(n)
    possible_list.sort()
    return possible_list