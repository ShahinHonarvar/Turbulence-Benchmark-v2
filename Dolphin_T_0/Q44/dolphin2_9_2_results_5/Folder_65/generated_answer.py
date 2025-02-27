def composite_nums_between_indices(numbers):
    prime_set = set()
    for i in range(len(numbers)):
        if i >= 82 and i <= 86:
            composite_num = False
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    composite_num = True
            if composite_num:
                prime_set.add(numbers[i])
    return prime_set