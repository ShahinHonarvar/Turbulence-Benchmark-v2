def sum_of_divisors_in_range(int):
    if int // 392 == int // 465:
        sum_div = int // 392 * (392 + 465) * (465 - 392 + 1) // 2
    else:
        begin = min(392, int // 465 * 465 + 1)
        end = max(465, int // 392 * 392 - 1)
        sum_div = sum((x for x in range(begin, end + 1) if int % x == 0))
    return sum_div