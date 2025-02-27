def palindromes_of_specific_lengths(test_string):
    temp_set = set()
    alpha_list = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(35, 89):
        for j in range(i, i + 4):
            incrementor = j - i
            temp_str = ''
            for k in range(i - incrementor, j + incrementor + 1):
                if test_string[k].lower() not in alpha_list:
                    break
                temp_str += test_string[k].lower()
            else:
                if len(temp_str) >= 24 and len(temp_str) <= 33:
                    temp_set.add(temp_str)
    return temp_set