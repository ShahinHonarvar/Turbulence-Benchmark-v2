def composite_nums_between_indices(input_list):
    try:
        found_composites = set()
        for i in range(34, 56):
            num = input_list[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        found_composites.add(num)
                        break
        return found_composites
    except IndexError:
        return set()