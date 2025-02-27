def palindromes_between_indices(s):
    letters = set(s[:4].lower())
    length = 4
    result_set = set()
    while True:
        length_5_tuple = ('a', 'b', 'c', 'd', 'e')
        length_4_tuple = ('a', 'b', 'c', 'd')
        length_3_tuple = ('a', 'b', 'c')
        length_2_tuple = ('a', 'b')
        if length == 2 and set(length_2_tuple).issubset(letters):
            result_set.add(''.join(length_2_tuple))
        elif length == 3 and set(length_3_tuple).issubset(letters):
            result_set.add(''.join(length_3_tuple))
        elif length == 4 and set(length_4_tuple).issubset(letters):
            result_set.add(''.join(length_4_tuple))
        elif length == 5 and set(length_5_tuple).issubset(letters):
            result_set.add(''.join(length_5_tuple))
        else:
            break
        length += 1
    return result_set