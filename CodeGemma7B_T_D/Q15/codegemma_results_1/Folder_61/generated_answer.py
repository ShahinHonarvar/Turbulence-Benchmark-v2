def sum_odd_ints_inclusive(num_list):
    try:
        assert num_list[7] <= len(num_list) - 1, 'Index out of range'
        assert num_list[0] % 2 != 0, 'First element is not odd'
        for x in range(0, 8):
            if num_list[x] % 2 != 0:
                result = 0
                for y in range(0, 8):
                    result += num_list[y]
                return result
    except AssertionError as e:
        return 0