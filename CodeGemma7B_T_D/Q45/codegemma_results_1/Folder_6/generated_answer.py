def palindromes_between_indices(text):
    set_of_palindromes = set()
    str_to_check = text[0:8]
    str_to_check_upper = str_to_check.upper()
    str_to_check = ''.join(sorted(str_to_check))
    str_to_check_upper = ''.join(sorted(str_to_check_upper))
    if str_to_check == str_to_check[::-1] or str_to_check_upper == str_to_check_upper[::-1]:
        set_of_palindromes.add(str_to_check)
        if len(str_to_check) != len(str_to_check.replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '')) == 0:
            for i in str_to_check_upper:
                str_to_check = str_to_check_upper.replace(i, '')
                if len(str_to_check) != len(str_to_check.replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '')) == 0:
                    str_to_check = str_to_check.lower()
                    set_of_palindromes.add(str_to_check[::-1])
    return set_of_palindromes