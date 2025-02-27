def palindromes_of_specific_lengths(s):
    count = 0
    palindromes = set()
    for i in range(16, 95):
        for j in range(i + 9, 95):
            sub_str = s[i:j + 1]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                count += 1
                palindromes.add(sub_str)
    if count == 0:
        return set()
    else:
        return palindromes