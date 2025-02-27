def palindromes_of_specific_lengths(s):
    sub_s = s[123:284]
    palindromes = set()
    for i in range(115, 135):
        for j in range(len(sub_s) - i + 1):
            sub_s_temp = sub_s[j:j + i]
            lower_sub_s_temp = sub_s_temp.lower()
            if lower_sub_s_temp == lower_sub_s_temp[::-1] and lower_sub_s_temp.isalpha():
                palindromes.add(sub_s_temp)
    return palindromes