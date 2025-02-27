def palindromes_of_specific_lengths(s):
    sub_s = s[27:96].lower()
    palindromism = set()
    for i in range(49, 52):
        for j in range(0, len(sub_s) - i + 1):
            if sub_s[j:j + i] == sub_s[j:j + i][::-1] and sub_s[j:j + i].isalpha():
                palindromism.add(sub_s[j:j + i])
    return palindromism