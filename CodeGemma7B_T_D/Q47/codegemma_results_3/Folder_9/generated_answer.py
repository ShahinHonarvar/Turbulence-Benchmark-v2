def palindromes_of_specific_lengths(str):
    lower_cased_str = str.lower()
    pals_set = set()
    for i in range(300):
        for j in range(50, 61):
            if i + j <= 300 and lower_cased_str[i:i + j] == lower_cased_str[i:i + j][::-1]:
                pals_set.add(lower_cased_str[i:i + j])
    return pals_set