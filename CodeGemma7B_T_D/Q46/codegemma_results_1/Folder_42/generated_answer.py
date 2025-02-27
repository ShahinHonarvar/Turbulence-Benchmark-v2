def gcf_three_nums(positives):
    answer = 1
    for prime in range(2, 101):
        while prime in positives and positives[19] % prime == 0 and (positives[69] % prime == 0) and (positives[97] % prime == 0):
            answer *= prime
            for i in (19, 69, 97):
                positives[i] //= prime
    return answer