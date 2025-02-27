def return_vowels(s):
    vowels = []
    for i in range(260, 322):
        if s[i] > '%' and s[i] <= 'U' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels