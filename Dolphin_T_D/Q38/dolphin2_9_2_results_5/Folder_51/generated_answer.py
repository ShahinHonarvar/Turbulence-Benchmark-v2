def find_subset_of_length_n(s):
    if len(s) == 0 or len(s) < 64:
        return 0
    else:
        result = 1
        for i in range(64, 0, -1):
            result *= len(s) + 1 - i
            for j in range(2, result + 1):
                if result % j == 0:
                    result = result / j
        return int(result)