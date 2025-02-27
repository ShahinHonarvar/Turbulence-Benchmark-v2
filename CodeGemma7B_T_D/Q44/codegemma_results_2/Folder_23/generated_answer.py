def composite_nums_between_indices(given_list):
    composite_set = set()
    for number in given_list[20:31]:
        if number != 1 and number not in [2, 3, 5, 7]:
            for i in range(1, number // 2 + 1):
                if number % i == 0:
                    composite_set.add(number)
                    break
    return composite_set