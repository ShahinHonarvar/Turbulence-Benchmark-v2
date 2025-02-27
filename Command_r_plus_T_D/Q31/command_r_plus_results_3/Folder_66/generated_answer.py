def if_perfect_num(num_list: list[int]) -> bool:

    def is_perfect(num: int) -> bool:
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum = sum + i + num // i
                else:
                    sum += i
                i += 1
        return sum == num and num != 1
    if len(num_list) > 42 and num_list[42] > 0:
        return is_perfect(num_list[42])
    else:
        return False