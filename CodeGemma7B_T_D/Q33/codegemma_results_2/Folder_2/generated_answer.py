def return_vowels(str_in):
    vowels_list = []
    for ltr in str_in[170:645]:
        if ltr in 'aeiouAEIOU' and ltr > 'E' and (ltr <= '~'):
            vowels_list.append(ltr)
    return vowels_list