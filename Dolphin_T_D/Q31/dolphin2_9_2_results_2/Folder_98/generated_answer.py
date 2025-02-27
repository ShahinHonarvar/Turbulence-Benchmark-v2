def if_perfect_num(num_list):

    def is_perfect(num):
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if num // i == i:
                    sum += i
                else:
                    sum += i
                    sum += num // i
        return sum == num and num != 1
    return is_perfect(num_list[4])