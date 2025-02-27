import sys
import heapq as hq

def all_left_right_truncatable_prime(x):
    if x <= 1:
        return []
    res = []
    for i in range(2, int(str(x)[0]) + 1):
        for j in range(2, str(x)[-1] + 1):
            if is_left_right_truncatable_prime(i, j):
                res.append(i ** 10 + j)
                break
    return sorted(res)

def is_left_right_truncatable_prime(i, j):
    return i > 1 and i ** 10 + j > 9 ** 9 or (i == 1 and j > 9)

def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        x = int(input())
        print(*all_left_right_truncatable_prime(x))