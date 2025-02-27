def palindromes_of_specific_lengths(str_in):
    all_palindromes = set()
    str_in = str_in.lower().strip()
    for i in range(len(str_in)):
        for j in [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]:
            if i - j + 1 >= 0 and i + j - 1 <= 300 and (str_in[i - j + 1:i + j] == str_in[i - j + 1:i + j][::-1]):
                all_palindromes.add(str_in[i - j + 1:i + j])
    return all_palindromes